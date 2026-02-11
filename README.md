# 🐄 Dairy Cow Hoof Analyzer

AI-powered web application for analyzing dairy cow hoof health and determining if trimming is needed.

## Features

- 📸 Upload images or capture from camera
- 🤖 AI-powered analysis using Claude Vision
- 📊 Assessment based on professional hoof trimming standards
- ✅ Clear recommendations (GOOD vs NEEDS TRIM)
- 💡 Detailed analysis of angle, toe length, and weight distribution

## Analysis Criteria

The app evaluates hooves based on:
- **Ideal angle**: 45-55° (optimal 50-60°)
- **Toe length**: ~3 inches
- **Weight distribution**: Even between claws
- **Common issues**: Under-run heel, club foot, overgrowth

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Anthropic API key ([get one here](https://console.anthropic.com/))

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

### 3. Configure API Key

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your Anthropic API key
# ANTHROPIC_API_KEY=sk-ant-api03-...
```

Or set it directly in your terminal:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

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

Based on Claude Vision API pricing:
- ~$0.01-0.05 per image analysis
- 100 images/month: ~$5/month
- 1,000 images/month: ~$30/month

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
