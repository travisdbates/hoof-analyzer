# 🚀 Deployment Guide - Access from Your Phone!

This guide shows how to deploy your Hoof Analyzer to the cloud so you can access it from your phone anywhere.

## Option 1: Deploy to Railway (Recommended - FREE)

Railway offers a free tier perfect for this app. It takes about 10 minutes.

### Step 1: Create GitHub Repository

```bash
# In the hoof-analyzer directory
git add .
git commit -m "Initial commit - Hoof Analyzer"

# Create a new repo on GitHub.com, then:
git remote add origin https://github.com/YOUR-USERNAME/hoof-analyzer.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Railway

1. Go to https://railway.app/
2. Click "Start a New Project"
3. Sign up with GitHub (it's free)
4. Click "Deploy from GitHub repo"
5. Select your `hoof-analyzer` repository
6. Railway will automatically detect it's a Python app

### Step 3: Add Your API Key

1. In Railway dashboard, click on your project
2. Go to "Variables" tab
3. Add a new variable:
   - Name: `ANTHROPIC_API_KEY`
   - Value: `your-api-key-here`
4. Click "Add"

### Step 4: Get Your URL

1. Go to "Settings" tab
2. Click "Generate Domain"
3. You'll get a URL like: `https://hoof-analyzer.up.railway.app`

**Done!** 🎉 Now you can access it from your phone at that URL!

---

## Option 2: Deploy to Render (Also FREE)

Similar to Railway, also has a free tier.

### Step 1: Push to GitHub (same as above)

### Step 2: Deploy to Render

1. Go to https://render.com/
2. Sign up (free)
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Configure:
   - **Name**: hoof-analyzer
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Add Environment Variable:
   - Key: `ANTHROPIC_API_KEY`
   - Value: your-api-key
7. Click "Create Web Service"

You'll get a URL like: `https://hoof-analyzer.onrender.com`

---

## Option 3: Quick Testing with ngrok (Temporary)

If you just want to test quickly without deploying:

```bash
# Install ngrok
brew install ngrok

# Start your app
./start.sh

# In another terminal
ngrok http 5000
```

You'll get a temporary URL like `https://abc123.ngrok-free.app` that expires when you close it.

---

## Using from Your Phone

Once deployed:

1. Open the URL in your phone's browser (Safari/Chrome)
2. Tap "Use Camera" button
3. Take a picture of the hoof
4. Tap "Analyze Hoof"
5. Get instant results!

**Pro tip**: Add the URL to your phone's home screen for quick access:
- **iPhone**: Safari → Share → Add to Home Screen
- **Android**: Chrome → Menu → Add to Home Screen

---

## Costs

- **Railway Free Tier**: 500 hours/month (plenty for testing)
- **Render Free Tier**: Spins down after inactivity (slower first load)
- **API Costs**: Same as before (~$0.01-0.05 per image)

For personal use, the free tiers should be more than enough!

---

## Troubleshooting

**App won't start:**
- Check that ANTHROPIC_API_KEY is set in environment variables
- Check deployment logs for errors

**Camera not working:**
- Make sure you're using HTTPS (not HTTP)
- Grant camera permissions in browser

**Slow response:**
- Free tier services may be slower
- First request after inactivity takes longer (Render)

---

## Security Note

Your app is now public! Consider adding:
- Password protection
- Rate limiting
- Usage tracking

Let me know if you need help adding these features!
