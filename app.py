import os
import base64
import concurrent.futures
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from anthropic import Anthropic
import google.generativeai as genai

app = Flask(__name__, static_folder='.')
CORS(app)

# Initialize API clients
anthropic_client = None
gemini_model = None

# Try to initialize Anthropic
if os.environ.get("ANTHROPIC_API_KEY"):
    anthropic_client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Try to initialize Gemini
if os.environ.get("GEMINI_API_KEY"):
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')

HOOF_ANALYSIS_PROMPT = """You are an expert dairy cattle hoof trimmer. Analyze this hoof image based on the following criteria:

IDEAL HOOF SPECIFICATIONS:
- Angle: 45-55° (optimal 50-60° for well-trimmed hooves)
- Toe length: approximately 3 inches
- Front feet: ~50° angle
- Hind feet: ~52° angle
- Flat sole with even weight distribution between inner and outer claws
- Straight dorsal wall

PROBLEMS TO IDENTIFY:
- Low angle (<40°): Under-run heel causing tendon/heel strain and lameness
- High angle: Club foot with excess pressure on toe and coffin joint
- Uneven weight distribution
- Overgrown horn on sole at toe
- Toe length over 3 inches
- Heel depth issues

Please analyze this hoof image and provide:

1. **Status**: State clearly if the hoof is "GOOD" or "NEEDS TRIM"
2. **Angle Assessment**: Estimate the hoof angle and whether it's within the ideal range
3. **Toe Length**: Assess if toe length appears appropriate (should be ~3 inches)
4. **Weight Distribution**: Comment on balance between claws
5. **Specific Issues**: List any problems you observe (overgrowth, under-run heel, etc.)
6. **Recommendations**: If trim is needed, specify what should be corrected

Be specific and practical in your assessment."""


def analyze_with_claude(image_data):
    """Analyze hoof image using Claude Vision API"""
    if not anthropic_client:
        raise Exception("Claude API key not configured")

    message = anthropic_client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": HOOF_ANALYSIS_PROMPT
                    }
                ],
            }
        ],
    )

    analysis = message.content[0].text
    status = "NEEDS TRIM" if "NEEDS TRIM" in analysis.upper() else "GOOD"

    return {
        'provider': 'Claude Sonnet 4.5',
        'status': status,
        'analysis': analysis,
        'success': True
    }


def analyze_with_gemini(image_data):
    """Analyze hoof image using Google Gemini API"""
    if not gemini_model:
        raise Exception("Gemini API key not configured")

    # Decode base64 image
    image_bytes = base64.b64decode(image_data)

    # Create the prompt with image
    response = gemini_model.generate_content([
        HOOF_ANALYSIS_PROMPT,
        {
            'mime_type': 'image/jpeg',
            'data': image_bytes
        }
    ])

    analysis = response.text
    status = "NEEDS TRIM" if "NEEDS TRIM" in analysis.upper() else "GOOD"

    return {
        'provider': 'Google Gemini 1.5 Flash',
        'status': status,
        'analysis': analysis,
        'success': True
    }


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/providers', methods=['GET'])
def get_providers():
    """Return available AI providers"""
    providers = []

    if anthropic_client:
        providers.append({
            'id': 'claude',
            'name': 'Claude Sonnet 4.5',
            'cost': '~$0.01-0.05 per image',
            'description': 'Anthropic Claude - High accuracy'
        })

    if gemini_model:
        providers.append({
            'id': 'gemini',
            'name': 'Google Gemini 1.5 Flash',
            'cost': 'FREE (15 req/min)',
            'description': 'Google Gemini - Fast and free'
        })

    return jsonify({
        'providers': providers,
        'success': True
    })


@app.route('/analyze', methods=['POST'])
def analyze_hoof():
    try:
        data = request.json
        image_data = data.get('image')
        provider = data.get('provider', 'claude')  # Default to Claude
        compare_mode = data.get('compare', False)

        if not image_data:
            return jsonify({'error': 'No image provided'}), 400

        # Remove data URL prefix if present
        if ',' in image_data:
            image_data = image_data.split(',')[1]

        # Compare mode: run both providers in parallel
        if compare_mode:
            results = {}
            errors = {}

            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                futures = {}

                if anthropic_client:
                    futures['claude'] = executor.submit(analyze_with_claude, image_data)

                if gemini_model:
                    futures['gemini'] = executor.submit(analyze_with_gemini, image_data)

                # Collect results
                for provider_id, future in futures.items():
                    try:
                        results[provider_id] = future.result()
                    except Exception as e:
                        errors[provider_id] = str(e)

            if not results:
                return jsonify({
                    'error': 'No providers available or all failed',
                    'details': errors,
                    'success': False
                }), 500

            return jsonify({
                'compare': True,
                'results': results,
                'errors': errors if errors else None,
                'success': True
            })

        # Single provider mode
        if provider == 'claude':
            if not anthropic_client:
                return jsonify({
                    'error': 'Claude API key not configured',
                    'success': False
                }), 400
            result = analyze_with_claude(image_data)
        elif provider == 'gemini':
            if not gemini_model:
                return jsonify({
                    'error': 'Gemini API key not configured',
                    'success': False
                }), 400
            result = analyze_with_gemini(image_data)
        else:
            return jsonify({
                'error': f'Unknown provider: {provider}',
                'success': False
            }), 400

        return jsonify(result)

    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


if __name__ == '__main__':
    # Check API keys
    if not os.environ.get("ANTHROPIC_API_KEY") and not os.environ.get("GEMINI_API_KEY"):
        print("⚠️  WARNING: No API keys configured!")
        print("Please set at least one:")
        print("  - ANTHROPIC_API_KEY for Claude")
        print("  - GEMINI_API_KEY for Google Gemini")
        print("\nGet your API keys:")
        print("  - Claude: https://console.anthropic.com/")
        print("  - Gemini: https://aistudio.google.com/app/apikey")
    else:
        if os.environ.get("ANTHROPIC_API_KEY"):
            print("✅ Claude API configured")
        if os.environ.get("GEMINI_API_KEY"):
            print("✅ Gemini API configured")

    # Get port from environment (for deployment) or use 5000 for local
    port = int(os.environ.get("PORT", 5000))
    # Disable debug in production
    debug = os.environ.get("FLASK_ENV") != "production"

    app.run(host='0.0.0.0', port=port, debug=debug)
