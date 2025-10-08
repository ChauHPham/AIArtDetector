import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Import the inference module
from src.inference import ArtDetector

app = Flask(__name__)
CORS(app)

# Global detector instance
detector = None

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict image class"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No image selected'}), 400
        
        # Read image bytes
        image_bytes = file.read()
        
        # Make prediction using the detector
        result = detector.predict(image_bytes)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': detector is not None,
        'device': str(detector.device) if detector else 'unknown'
    })

def load_detector(checkpoint_path='models/detector.pth'):
    """Load the AI Art Detector"""
    global detector
    detector = ArtDetector(checkpoint_path)
    return detector

if __name__ == '__main__':
    # Load detector on startup
    load_detector()
    app.run(debug=True, host='0.0.0.0', port=5000)
