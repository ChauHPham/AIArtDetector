#!/usr/bin/env python3
"""
Test a single image from the dataset to see if detection works
"""
import argparse
import sys
from pathlib import Path
from src.inference import ArtDetector

def test_image(image_path, checkpoint='models/detector.pth'):
    """Test a single image and show the prediction"""
    
    # Load the detector
    print(f"Loading model from {checkpoint}...")
    detector = ArtDetector(checkpoint)
    print(f"✓ Model loaded on {detector.device}\n")
    
    # Check if image exists
    if not Path(image_path).exists():
        print(f"✗ Error: Image not found at {image_path}")
        return
    
    # Make prediction
    print(f"Testing image: {image_path}")
    print("-" * 50)
    
    try:
        result = detector.predict_from_file(image_path)
        
        print(f"\n🎯 Prediction: {result['predicted_class']}")
        print(f"📊 Confidence: {result['confidence']:.2%}")
        print(f"\n📈 All Probabilities:")
        for class_name, prob in result['probabilities'].items():
            bar_length = int(prob * 30)
            bar = "█" * bar_length + "░" * (30 - bar_length)
            print(f"  {class_name:8s}: {prob:.4f} ({prob:.2%}) {bar}")
        
        # Determine if it's correct (if we know the true label from path)
        if 'AI' in image_path or '/AI/' in image_path:
            true_label = 'AI'
        elif 'Human' in image_path or '/Human/' in image_path:
            true_label = 'Human'
        else:
            true_label = None
        
        if true_label:
            is_correct = result['predicted_class'] == true_label
            status = "✓ CORRECT" if is_correct else "✗ INCORRECT"
            print(f"\n{'='*50}")
            print(f"True Label: {true_label}")
            print(f"Prediction: {result['predicted_class']}")
            print(f"Result: {status}")
            print(f"{'='*50}")
        
    except Exception as e:
        print(f"✗ Error predicting image: {e}")
        import traceback
        traceback.print_exc()

def main():
    parser = argparse.ArgumentParser(description='Test a single image with the AI Art Detector')
    parser.add_argument('image_path', type=str, help='Path to the image file to test')
    parser.add_argument('--checkpoint', type=str, default='models/detector.pth',
                       help='Path to model checkpoint (default: models/detector.pth)')
    
    args = parser.parse_args()
    test_image(args.image_path, args.checkpoint)

if __name__ == '__main__':
    main()

