#!/usr/bin/env python3
"""
Test script for the web application
"""
import requests
import os
from PIL import Image
import io

def create_test_image():
    """Create a simple test image"""
    # Create a simple RGB image
    img = Image.new('RGB', (224, 224), color='red')
    
    # Convert to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    
    return img_byte_arr.getvalue()

def test_health_endpoint(base_url='http://localhost:5000'):
    """Test the health endpoint"""
    try:
        response = requests.get(f'{base_url}/health')
        if response.status_code == 200:
            data = response.json()
            print("✓ Health check passed")
            print(f"  Status: {data['status']}")
            print(f"  Model loaded: {data['model_loaded']}")
            print(f"  Device: {data['device']}")
            return True
        else:
            print(f"✗ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to server. Make sure the web app is running.")
        return False

def test_prediction_endpoint(base_url='http://localhost:5000'):
    """Test the prediction endpoint"""
    try:
        # Create test image
        test_image = create_test_image()
        
        # Prepare files for upload
        files = {'image': ('test.jpg', test_image, 'image/jpeg')}
        
        # Make prediction request
        response = requests.post(f'{base_url}/predict', files=files)
        
        if response.status_code == 200:
            data = response.json()
            print("✓ Prediction test passed")
            print(f"  Predicted class: {data['predicted_class']}")
            print(f"  Confidence: {data['confidence']:.3f}")
            print("  Probabilities:")
            for class_name, prob in data['probabilities'].items():
                print(f"    {class_name}: {prob:.3f}")
            return True
        else:
            print(f"✗ Prediction test failed: {response.status_code}")
            print(f"  Response: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to server. Make sure the web app is running.")
        return False

def main():
    print("Testing AI Art Detector Web Application")
    print("=" * 50)
    
    # Test health endpoint
    print("\n1. Testing health endpoint...")
    health_ok = test_health_endpoint()
    
    # Test prediction endpoint
    print("\n2. Testing prediction endpoint...")
    prediction_ok = test_prediction_endpoint()
    
    # Summary
    print("\n" + "=" * 50)
    if health_ok and prediction_ok:
        print("✓ All tests passed! The web application is working correctly.")
    else:
        print("✗ Some tests failed. Check the output above for details.")
        print("\nTo start the web application, run:")
        print("  python run_web.py")

if __name__ == '__main__':
    main()
