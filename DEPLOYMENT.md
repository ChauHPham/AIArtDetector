# 🚀 Deployment Guide - AI Art Detector

This guide will help you deploy your AI Art Detector web application to a live website.

## 📋 Prerequisites

1. **Trained Model**: Make sure you have `models/detector.pth` trained and ready
2. **Git Repository**: Your code should be in a Git repository
3. **Account**: Sign up for one of the deployment platforms below

## 🌐 Deployment Options

### Option 1: Render (Recommended - Free Tier Available)

**Pros:**
- Free tier available
- Easy deployment from GitHub
- Automatic HTTPS
- Supports Python/Flask apps

**Steps:**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Create `render.yaml`** (I'll create this for you)

3. **Deploy on Render:**
   - Go to https://render.com
   - Sign up/login
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository
   - Configure:
     - **Name**: ai-art-detector
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
     - **Instance Type**: Free (or paid for better performance)

4. **Environment Variables** (if needed):
   - Add any environment variables in Render dashboard

5. **Deploy!**
   - Click "Create Web Service"
   - Wait for build to complete
   - Your app will be live at `https://your-app-name.onrender.com`

---

### Option 2: Railway (Easy & Fast)

**Pros:**
- Very easy setup
- Free tier with $5 credit
- Automatic deployments from GitHub

**Steps:**

1. **Push to GitHub** (same as above)

2. **Deploy on Railway:**
   - Go to https://railway.app
   - Sign up/login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect Flask app
   - Add environment variable: `PORT=5000` (if needed)

3. **Configure Start Command:**
   - In Railway dashboard, go to Settings
   - Set start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

4. **Deploy!**
   - Railway will automatically deploy
   - Your app will be live at `https://your-app-name.up.railway.app`

---

### Option 3: Heroku (Classic Choice)

**Pros:**
- Well-established platform
- Good documentation
- Free tier available (with limitations)

**Steps:**

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Or download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create `Procfile`** (I'll create this for you)

3. **Login and Deploy:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

4. **Set Config Vars** (if needed):
   ```bash
   heroku config:set PYTHONPATH=/app
   ```

5. **Open your app:**
   ```bash
   heroku open
   ```

---

### Option 4: Hugging Face Spaces (Great for ML Apps)

**Pros:**
- Free GPU available
- Perfect for ML/AI apps
- Easy sharing

**Steps:**

1. **Install Hugging Face Hub:**
   ```bash
   pip install huggingface_hub
   ```

2. **Create Space:**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Docker" or "Gradio" (we'll adapt for Flask)

3. **Push your code:**
   ```bash
   git clone https://huggingface.co/spaces/your-username/your-space-name
   # Copy your files
   git push
   ```

**Note:** Hugging Face Spaces works best with Gradio. You might want to create a Gradio wrapper.

---

### Option 5: AWS/GCP/Azure (Production Scale)

**For AWS (EC2/Elastic Beanstalk):**
- More complex setup
- Better for production
- Pay-as-you-go pricing

**For Google Cloud Platform:**
- App Engine or Cloud Run
- Good for Python apps
- Free tier available

**For Azure:**
- App Service
- Easy Flask deployment
- Free tier available

---

## 📝 Files Needed for Deployment

I'll create these files for you:

1. **`Procfile`** - For Heroku/Railway
2. **`runtime.txt`** - Python version specification
3. **`.gitignore`** - Exclude unnecessary files
4. **`render.yaml`** - For Render deployment

---

## 🔧 Important Notes

### Model File Size
- Your `models/detector.pth` is ~90MB
- Some free tiers have file size limits
- Consider:
  - Using Git LFS for large files
  - Storing model in cloud storage (S3, etc.)
  - Loading model from URL on startup

### Environment Variables
You might want to add:
```bash
FLASK_ENV=production
PORT=5000
MODEL_PATH=models/detector.pth
```

### Dependencies
Make sure `requirements.txt` includes:
- `gunicorn` (for production server)
- All your dependencies

---

## 🚀 Quick Start (Render - Easiest)

1. **Push code to GitHub**
2. **Go to render.com**
3. **Create new Web Service**
4. **Connect GitHub repo**
5. **Deploy!**

That's it! Your app will be live in ~5 minutes.

---

## 📊 Monitoring

After deployment:
- Monitor logs in your platform's dashboard
- Set up error tracking (Sentry, etc.)
- Monitor performance and usage

---

## 🔒 Security Considerations

1. **Rate Limiting**: Add rate limiting to prevent abuse
2. **File Size Limits**: Limit upload size
3. **CORS**: Configure CORS properly
4. **HTTPS**: Most platforms provide this automatically

---

## 💡 Tips

- **Start with free tier** to test
- **Use environment variables** for configuration
- **Monitor your usage** to avoid unexpected costs
- **Set up CI/CD** for automatic deployments
- **Use a CDN** for static assets if needed

---

## 🆘 Troubleshooting

**Build fails:**
- Check Python version compatibility
- Verify all dependencies in `requirements.txt`
- Check build logs for errors

**App crashes:**
- Check application logs
- Verify model file is included
- Check environment variables

**Slow performance:**
- Upgrade to paid tier
- Optimize model size
- Use caching

---

## 📞 Need Help?

- Check platform-specific documentation
- Review application logs
- Test locally first with `gunicorn app:app`

Good luck with your deployment! 🎉

