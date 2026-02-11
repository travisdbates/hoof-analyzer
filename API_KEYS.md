# 🔑 Getting Your API Keys

This guide shows you how to get FREE API keys for both Google Gemini and Claude (optional).

## Google Gemini API (Recommended - FREE!)

### Step 1: Get Your Gemini API Key

1. Go to: **https://aistudio.google.com/app/apikey**
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the API key (starts with `AIza...`)

### Step 2: Add to Your App

**For local development:**
```bash
export GEMINI_API_KEY='your-key-here'
```

**For Railway/Render deployment:**
Add as environment variable:
- **Name**: `GEMINI_API_KEY`
- **Value**: Your Gemini API key

### Free Tier Limits

- ✅ **Gemini 1.5 Flash**: 15 requests/minute, 1 million tokens/day - FREE
- ✅ No credit card required
- ✅ Perfect for testing and personal use

---

## Claude API (Optional - Paid)

If you want to compare results or prefer Claude:

### Step 1: Get Your Claude API Key

1. Go to: **https://console.anthropic.com/**
2. Sign up for an account
3. Go to **API Keys** section
4. Click **"Create Key"**
5. Copy the API key (starts with `sk-ant-api...`)

### Step 2: Add to Your App

**For local development:**
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

**For Railway/Render deployment:**
Add as environment variable:
- **Name**: `ANTHROPIC_API_KEY`
- **Value**: Your Claude API key

### Pricing

- 💰 ~$0.01-0.05 per image
- 🎁 $5 free credits when you sign up
- 📊 Higher accuracy for complex cases

---

## Using Both (Comparison Mode)

You can configure both API keys to enable the **"Compare Both"** feature, which runs both AIs and shows you side-by-side results!

**Local development:**
```bash
export GEMINI_API_KEY='your-gemini-key'
export ANTHROPIC_API_KEY='your-claude-key'
```

**Railway/Render deployment:**
Add both as separate environment variables.

---

## Recommendations

### For Testing & Personal Use:
- ✅ **Use Gemini only** - It's completely FREE!
- You can analyze 15 hooves per minute, 1000s per day
- No credit card needed

### For Professional/Commercial Use:
- 💡 **Use both and compare** - See which works better for your needs
- Claude may provide more detailed analysis in some cases
- Gemini is faster and free, great for bulk processing

### For Maximum Flexibility:
- 🔄 **Configure both** - Switch between them or compare side-by-side
- Use Gemini for routine checks
- Use Claude for complex or uncertain cases
- Let the comparison mode help you decide which to trust

---

## Quick Start

1. Get your Gemini API key (2 minutes, free)
2. Add it to Railway environment variables
3. Start analyzing hooves immediately!

You can always add the Claude API key later if you want to compare results.
