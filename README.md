# AI Art Detector (PyTorch + Web App)

Detect whether an image is **AI-generated** or **Human-made** using a transfer-learning baseline.

## Features
- PyTorch + torchvision baseline (ResNet-50)
- Clean dataset loader with train/val splits
- Confusion matrix and classification report
- Ready-to-run CLI (`train.py`, `evaluate.py`)
- Jupyter notebook quickstart
- **🌐 Web Application** with Flask backend and modern HTML/JS frontend
- **🐳 Docker deployment** ready
- **📱 Responsive UI** with drag-and-drop image upload

## Folder Layout
```
ai_art_detector/
├─ data/
│  ├─ train/
│  │  ├─ AI/            # put AI-generated images here
│  │  └─ Human/         # put human-made images here
│  └─ val/
│     ├─ AI/
│     └─ Human/
├─ src/
│  ├─ datasets.py
│  ├─ model.py
│  ├─ train.py
│  ├─ evaluate.py
│  └─ inference.py      # model inference utilities
├─ templates/
│  └─ index.html        # web application frontend
├─ notebooks/
│  └─ quickstart.ipynb
├─ app.py               # Flask web application
├─ run_web.py           # web app startup script
├─ requirements.txt
├─ environment.yml
├─ Dockerfile
├─ docker-compose.yml
└─ README.md
```

## Quickstart
1. **Create environment**
   ```bash
   # Option A: conda
   conda env create -f environment.yml
   conda activate ai-art-detector

   # Option B: pip
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Add data**
   Place your images inside the `data/train/*` and `data/val/*` folders as shown above.

3. **Train**
   ```bash
   python -m src.train --data_dir data --epochs 10 --batch_size 32 --lr 1e-4 --num_classes 2
   ```

4. **Evaluate**
   ```bash
   python -m src.evaluate --data_dir data --checkpoint models/detector.pth --num_classes 2
   ```

## 🌐 Web Application

### Quick Start
1. **Install dependencies** (includes Flask and web dependencies)
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the web application**
   ```bash
   python run_web.py
   ```

3. **Open your browser** and go to `http://localhost:5000`

### Web App Features
- **Drag & Drop Interface**: Upload images by dragging them onto the upload area
- **Real-time Predictions**: Get instant AI/Human classification
- **Confidence Scores**: See probability distributions for all classes
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Image Preview**: See your uploaded image before analysis

### API Endpoints
- `GET /` - Main web interface
- `POST /predict` - Upload image and get prediction
- `GET /health` - Health check endpoint

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t ai-art-detector .
docker run -p 5000:5000 ai-art-detector
```

## 📥 Download Dataset

You can download the dataset using either method:

### Option 1: Using KaggleHub (Recommended)
```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("alessandrasala79/ai-vs-human-generated-dataset")
print("Path to dataset files:", path)
```

**Pros:**
- Clean, programmatic download
- Easy to update to latest version
- Handles authentication automatically

**Requirements:**
- Install: `pip install kagglehub`
- Set up Kaggle API credentials (kaggle.json in ~/.kaggle/)

### Option 2: Manual Download
1. Go to: https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset
2. Click "Download" button
3. Extract the zip file
4. Organize images into `data/train/AI/`, `data/train/Human/`, `data/val/AI/`, `data/val/Human/`

**Pros:**
- No API setup needed
- Can preview dataset before downloading

## 🌐 Deploy to Production

Want to make this a live website? See the deployment guides:

- **Quick Start**: See `DEPLOY_QUICKSTART.md` for the fastest way to deploy
- **Full Guide**: See `DEPLOYMENT.md` for detailed deployment options

**Recommended platforms:**
- **Render** (Free tier available) - Easiest
- **Railway** (Free $5 credit) - Very simple
- **Heroku** (Free tier with limitations) - Classic choice

## Notes
- This is a baseline; for real-world robustness, consider:
  - multiple generators in the AI class
  - augmentations (jpeg, resize, blur) to avoid overfitting to trivial cues
- GPU recommended but not required.
- Web app works with or without a trained model (will use untrained weights if no checkpoint found)
- **Disclaimer**: Predictions may not be accurate due to model limitations, potential overfitting, and limited training data. Use for educational purposes only.
