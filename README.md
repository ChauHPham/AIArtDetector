# AI Art & Protection Detector (PyTorch + Web App)

Detect whether an image is **AI-generated**, **Human-made**, or **Protected** (e.g., Glaze/Nightshade-like perturbations) using a transfer-learning baseline.

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
│  │  ├─ Human/         # put human-made images here
│  │  └─ Protected/     # put Glaze/Nightshade protected images here
│  └─ val/
│     ├─ AI/
│     ├─ Human/
│     └─ Protected/
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
   python -m src.train --data_dir data --epochs 10 --batch_size 32 --lr 1e-4 --num_classes 3
   ```

4. **Evaluate**
   ```bash
   python -m src.evaluate --data_dir data --checkpoint models/detector.pth --num_classes 3
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
- **Real-time Predictions**: Get instant AI/Human/Protected classification
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

## Notes
- This is a baseline; for real-world robustness, consider:
  - multiple generators in the AI class
  - augmentations (jpeg, resize, blur) to avoid overfitting to trivial cues
  - a protection detector head that uses high-frequency residuals
- GPU recommended but not required.
- Web app works with or without a trained model (will use untrained weights if no checkpoint found)
