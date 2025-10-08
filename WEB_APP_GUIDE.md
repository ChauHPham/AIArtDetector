# 🌐 AI Art Detector Web Application Guide

Your PyTorch AI art detector has been successfully transformed into a modern web application! Here's everything you need to know.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Web App
```bash
python run_web.py
```

### 3. Open Your Browser
Go to `http://localhost:5000` and start detecting AI art!

## 📁 What's New

### New Files Created
- `app.py` - Flask web application backend
- `templates/index.html` - Modern, responsive frontend
- `src/inference.py` - Model inference utilities
- `run_web.py` - Easy startup script
- `test_web.py` - Test script for the web app
- `Dockerfile` - Docker container configuration
- `docker-compose.yml` - Docker Compose setup
- `.dockerignore` - Docker ignore file

### Updated Files
- `requirements.txt` - Added Flask and web dependencies
- `README.md` - Added web application documentation

## 🎨 Web App Features

### Frontend (HTML/JS)
- **Modern UI**: Beautiful gradient design with smooth animations
- **Drag & Drop**: Upload images by dragging them onto the upload area
- **Image Preview**: See your uploaded image before analysis
- **Real-time Results**: Instant predictions with confidence scores
- **Probability Bars**: Visual representation of all class probabilities
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Error Handling**: Clear error messages for troubleshooting

### Backend (Flask)
- **RESTful API**: Clean endpoints for predictions and health checks
- **Model Integration**: Seamlessly uses your existing PyTorch model
- **Error Handling**: Robust error handling and validation
- **CORS Support**: Ready for cross-origin requests
- **Health Monitoring**: Built-in health check endpoint

## 🔧 API Endpoints

### `GET /`
Serves the main web interface.

### `POST /predict`
Upload an image and get AI/Human/Protected classification.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: `image` file

**Response:**
```json
{
  "predicted_class": "AI",
  "confidence": 0.95,
  "probabilities": {
    "AI": 0.95,
    "Human": 0.03,
    "Protected": 0.02
  }
}
```

### `GET /health`
Check application health and model status.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "device": "cuda:0"
}
```

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)
```bash
docker-compose up --build
```

### Manual Docker Build
```bash
docker build -t ai-art-detector .
docker run -p 5000:5000 ai-art-detector
```

## 🧪 Testing

### Test the Web Application
```bash
python test_web.py
```

This will test both the health endpoint and prediction functionality.

### Manual Testing
1. Start the web app: `python run_web.py`
2. Open `http://localhost:5000` in your browser
3. Upload an image and see the results!

## 🔧 Configuration

### Model Checkpoint
By default, the app looks for `models/detector.pth`. You can specify a different path:

```bash
python run_web.py --checkpoint path/to/your/model.pth
```

### Server Configuration
```bash
python run_web.py --host 0.0.0.0 --port 8080 --debug
```

## 🎯 Usage Examples

### Command Line
```bash
# Start with default settings
python run_web.py

# Start with custom checkpoint
python run_web.py --checkpoint models/my_model.pth

# Start in debug mode
python run_web.py --debug

# Start on different port
python run_web.py --port 8080
```

### Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## 🔍 Troubleshooting

### Common Issues

1. **"Model checkpoint not found"**
   - Train a model first: `python -m src.train`
   - Or specify a different checkpoint path

2. **"Cannot connect to server"**
   - Make sure the web app is running: `python run_web.py`
   - Check if port 5000 is available

3. **"Import errors"**
   - Install dependencies: `pip install -r requirements.txt`
   - Make sure you're in the project directory

4. **"CUDA out of memory"**
   - The app will automatically fall back to CPU
   - Or reduce batch size in training

### Performance Tips

1. **GPU Acceleration**: The app automatically uses GPU if available
2. **Model Caching**: The model is loaded once at startup for fast inference
3. **Image Optimization**: Images are automatically resized to 224x224 for inference

## 🚀 Next Steps

### Enhancements You Can Add
1. **Batch Processing**: Upload multiple images at once
2. **Model Comparison**: Test different model checkpoints
3. **History**: Save prediction history
4. **Export Results**: Download results as CSV/JSON
5. **Advanced UI**: Add more visualization options
6. **Authentication**: Add user login system
7. **Database**: Store predictions and user data

### Deployment Options
1. **Cloud Platforms**: Deploy to AWS, GCP, or Azure
2. **Hugging Face Spaces**: Easy deployment with GPU support
3. **Heroku**: Simple deployment (though limited GPU)
4. **Self-hosted**: Use your own server with Docker

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Run the test script: `python test_web.py`
3. Check the console output for error messages
4. Make sure all dependencies are installed

Your AI art detector is now a fully functional web application! 🎉
