# 🚀 Quick Deployment Guide

## Easiest Option: Render (Free Tier)

### Step 1: Push to GitHub

```bash
# Make sure you're in the project directory
cd /Users/hoang/Downloads/ai_art_detector

# Initialize git if not already done
git init
git add .
git commit -m "Initial commit - AI Art Detector"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 2: Deploy on Render

1. **Go to https://render.com** and sign up (free)

2. **Click "New +" → "Web Service"**

3. **Connect your GitHub account** and select your repository

4. **Configure the service:**
   - **Name**: `ai-art-detector` (or any name you like)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Plan**: Free (or upgrade for better performance)

5. **Click "Create Web Service"**

6. **Wait for deployment** (~5-10 minutes)

7. **Your app is live!** 🎉
   - URL will be: `https://ai-art-detector.onrender.com` (or your custom name)

---

## Important: Model File

Your `models/detector.pth` file is ~90MB. For deployment, you need to include it. Here are your options:

### Option A: Include in Git (Simplest)
```bash
# Temporarily allow model files in git
# Edit .gitignore and comment out or remove the models/ line:
# # models/
# # *.pth

# Then commit the model
git add models/detector.pth
git commit -m "Add trained model for deployment"
git push
```

**Note:** After deployment, you can uncomment those lines in `.gitignore` again.

### Option B: Use Git LFS (Recommended for large files)
```bash
# Install Git LFS
brew install git-lfs  # macOS
# or download from https://git-lfs.github.com

# Initialize Git LFS
git lfs install
git lfs track "*.pth"
git add .gitattributes
git add models/detector.pth
git commit -m "Add model with Git LFS"
git push
```

### Option C: Store in Cloud Storage (Advanced)
- Upload model to AWS S3, Google Cloud Storage, etc.
- Download on app startup
- More complex but better for very large files

---

## Alternative: Railway (Also Easy)

1. **Go to https://railway.app**
2. **Sign up with GitHub**
3. **Click "New Project" → "Deploy from GitHub repo"**
4. **Select your repository**
5. **Railway auto-detects Flask** - just deploy!
6. **Your app is live!**

---

## After Deployment

1. **Test your live URL** - upload an image and verify it works
2. **Share the link** with others
3. **Monitor usage** in your platform's dashboard

---

## Troubleshooting

**Build fails?**
- Check that `requirements.txt` has all dependencies
- Verify Python version in `runtime.txt` matches your local version
- Check build logs in Render/Railway dashboard

**App crashes?**
- Check application logs
- Verify model file is included in deployment
- Make sure `models/detector.pth` exists

**Slow performance?**
- Free tiers have limited resources
- Consider upgrading to paid tier
- Optimize model size if needed

---

## That's It! 🎉

Your AI Art Detector is now a live website that anyone can access!

