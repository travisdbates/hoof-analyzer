# 🐄 Dairy Cow Hoof Analyzer

AI-powered web application for analyzing dairy cow hoof health and determining if trimming is needed.

## Features

- 📸 Upload images or capture from camera
- 🤖 **Multiple AI providers**: Choose between Google Gemini (FREE) or Claude
- 🔄 **Compare mode**: Run both AIs side-by-side and compare results
- 📊 Assessment based on professional hoof trimming standards
- ✅ Clear recommendations (GOOD vs NEEDS TRIM)
- 💡 Detailed analysis of angle, toe length, and weight distribution
- 📱 Mobile-friendly with camera capture
- ☁️ Cloud-ready for deployment

## Analysis Criteria

The app evaluates hooves based on:
- **Ideal angle**: 45-55° (optimal 50-60°)
- **Toe length**: ~3 inches
- **Weight distribution**: Even between claws
- **Common issues**: Under-run heel, club foot, overgrowth

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- At least one API key:
  - **Google Gemini API** (Recommended - FREE!) - [Get it here](https://aistudio.google.com/app/apikey)
  - **Anthropic Claude API** (Optional - Paid) - [Get it here](https://console.anthropic.com/)
  - See [API_KEYS.md](API_KEYS.md) for detailed instructions

### 2. Installation

```bash
# Navigate to project directory
cd hoof-analyzer

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your API key(s)
# You only need one, but can add both!
```

**Option A - Gemini only (FREE):**
```bash
export GEMINI_API_KEY='your-gemini-key-here'
```

**Option B - Claude only (Paid):**
```bash
export ANTHROPIC_API_KEY='your-claude-key-here'
```

**Option C - Both (for comparison):**
```bash
export GEMINI_API_KEY='your-gemini-key-here'
export ANTHROPIC_API_KEY='your-claude-key-here'
```

See [API_KEYS.md](API_KEYS.md) for detailed setup instructions.

### 4. Run the Application

```bash
python app.py
```

The app will start on `http://localhost:5000`

### 5. Use the App

1. Open your browser to `http://localhost:5000`
2. Upload a hoof image or capture one with your camera
3. Click "Analyze Hoof"
4. View the results and recommendations

## Cost Estimate

### Google Gemini (Recommended)
- ✅ **FREE**: 15 requests/minute, 1M tokens/day
- Perfect for personal use and testing
- No credit card required

### Claude (Optional)
- 💰 ~$0.01-0.05 per image analysis
- 100 images/month: ~$5/month
- 1,000 images/month: ~$30/month
- $5 free credits on signup

### Compare Mode
- Uses both APIs (free + paid)
- Great for validating results

## Project Structure

```
hoof-analyzer/
├── app.py              # Flask backend with Claude API integration
├── index.html          # Frontend web interface
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
└── README.md          # This file
```

## Troubleshooting

**API Key Error:**
- Make sure your `ANTHROPIC_API_KEY` is set in `.env` or environment
- Verify the key is valid at https://console.anthropic.com/

**CORS Error:**
- Make sure Flask is running on port 5000
- Check that flask-cors is installed

**Image Upload Issues:**
- Supported formats: JPG, PNG, WEBP
- Maximum file size: ~5MB recommended

## Future Enhancements

- [ ] Save analysis history
- [ ] Compare before/after trim images
- [ ] Track hoof health over time per cow
- [ ] Mobile app version
- [ ] Batch processing
- [ ] Custom ML model for offline use

## License

MIT License - Feel free to use and modify for your needs!
