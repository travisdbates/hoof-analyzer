import os
import base64
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from anthropic import Anthropic

app = Flask(__name__, static_folder='.')
CORS(app)

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

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


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/analyze', methods=['POST'])
def analyze_hoof():
    try:
        data = request.json
        image_data = data.get('image')

        if not image_data:
            return jsonify({'error': 'No image provided'}), 400

        # Remove data URL prefix if present
        if ',' in image_data:
            image_data = image_data.split(',')[1]

        # Call Claude Vision API
        message = client.messages.create(
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

        # Determine status from analysis
        status = "NEEDS TRIM" if "NEEDS TRIM" in analysis.upper() else "GOOD"

        return jsonify({
            'status': status,
            'analysis': analysis,
            'success': True
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


if __name__ == '__main__':
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("WARNING: ANTHROPIC_API_KEY not set in environment")
        print("Please set it with: export ANTHROPIC_API_KEY='your-key-here'")

    # Get port from environment (for deployment) or use 5000 for local
    port = int(os.environ.get("PORT", 5000))
    # Disable debug in production
    debug = os.environ.get("FLASK_ENV") != "production"

    app.run(host='0.0.0.0', port=port, debug=debug)
