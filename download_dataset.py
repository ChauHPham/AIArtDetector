#!/usr/bin/env python3
"""
Download and organize the AI vs Human dataset from Kaggle
"""
import os
import shutil
import argparse
import csv
from pathlib import Path

def download_via_kagglehub(dataset_name="alessandrasala79/ai-vs-human-generated-dataset"):
    """Download dataset using kagglehub"""
    try:
        import kagglehub
        print(f"Downloading dataset: {dataset_name}")
        path = kagglehub.dataset_download(dataset_name)
        print(f"✓ Dataset downloaded to: {path}")
        return path
    except ImportError:
        print("✗ kagglehub not installed. Install it with: pip install kagglehub")
        return None
    except Exception as e:
        print(f"✗ Error downloading dataset: {e}")
        return None

def organize_dataset(download_path, target_dir="data", val_split=0.2):
    """
    Organize downloaded dataset into train/val splits with AI/Human folders
    
    This handles the Kaggle dataset structure with CSV files:
    - train.csv: maps file_name to label (0=Human, 1=AI)
    - train_data/: folder with training images
    - test.csv: maps file_name to label for validation
    - test_data_v2/: folder with test images
    """
    target_path = Path(target_dir)
    train_ai = target_path / "train" / "AI"
    train_human = target_path / "train" / "Human"
    val_ai = target_path / "val" / "AI"
    val_human = target_path / "val" / "Human"
    
    # Create directories
    for dir_path in [train_ai, train_human, val_ai, val_human]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    download_path = Path(download_path)
    
    # Check for CSV-based structure (Kaggle dataset)
    train_csv = download_path / "train.csv"
    test_csv = download_path / "test.csv"
    train_data_dir = download_path / "train_data"
    test_data_dir = download_path / "test_data_v2"
    
    if train_csv.exists() and train_data_dir.exists():
        print("Detected CSV-based dataset structure")
        print("Organizing training set from train.csv...")
        
        # Process training data
        train_ai_count = 0
        train_human_count = 0
        
        with open(train_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                file_name = row['file_name']
                label = int(row['label'])
                
                # Label 0 = Human, Label 1 = AI
                source_path = download_path / file_name
                
                if source_path.exists():
                    if label == 1:  # AI
                        dest_path = train_ai / Path(file_name).name
                        shutil.copy2(source_path, dest_path)
                        train_ai_count += 1
                    else:  # Human (label == 0)
                        dest_path = train_human / Path(file_name).name
                        shutil.copy2(source_path, dest_path)
                        train_human_count += 1
        
        print(f"  ✓ Copied {train_ai_count} AI images and {train_human_count} Human images to train/")
        
        # Split training data into train/val (80/20 split)
        print("Splitting training data into train/val (80/20)...")
        import random
        random.seed(42)  # For reproducibility
        
        # Get all files
        train_ai_files = list(train_ai.glob('*.jpg')) + list(train_ai.glob('*.jpeg')) + list(train_ai.glob('*.png'))
        train_human_files = list(train_human.glob('*.jpg')) + list(train_human.glob('*.jpeg')) + list(train_human.glob('*.png'))
        
        # Shuffle
        random.shuffle(train_ai_files)
        random.shuffle(train_human_files)
        
        # Split 80/20
        split_idx_ai = int(len(train_ai_files) * 0.8)
        split_idx_human = int(len(train_human_files) * 0.8)
        
        val_ai_count = 0
        val_human_count = 0
        
        # Move validation AI images
        for img_file in train_ai_files[split_idx_ai:]:
            dest_path = val_ai / img_file.name
            shutil.move(str(img_file), str(dest_path))
            val_ai_count += 1
        
        # Move validation Human images
        for img_file in train_human_files[split_idx_human:]:
            dest_path = val_human / img_file.name
            shutil.move(str(img_file), str(dest_path))
            val_human_count += 1
        
        print(f"  ✓ Moved {val_ai_count} AI images and {val_human_count} Human images to val/")
    
    else:
        # Fallback to folder-based structure
        print("Trying folder-based structure...")
        if (download_path / "train").exists():
            train_dir = download_path / "train"
            val_dir = download_path / "val" if (download_path / "val").exists() else download_path / "test"
            
            if (train_dir / "AI").exists() and (train_dir / "Human").exists():
                print("Organizing train set...")
                shutil.copytree(train_dir / "AI", train_ai, dirs_exist_ok=True)
                shutil.copytree(train_dir / "Human", train_human, dirs_exist_ok=True)
                
                if val_dir.exists():
                    print("Organizing validation set...")
                    if (val_dir / "AI").exists() and (val_dir / "Human").exists():
                        shutil.copytree(val_dir / "AI", val_ai, dirs_exist_ok=True)
                        shutil.copytree(val_dir / "Human", val_human, dirs_exist_ok=True)
    
    # Count actual image files (excluding .gitkeep)
    def count_images(folder):
        return len([f for f in folder.glob('*') if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp']])
    
    print(f"\n✓ Dataset organized in {target_dir}/")
    print(f"  Train AI: {count_images(train_ai)} images")
    print(f"  Train Human: {count_images(train_human)} images")
    print(f"  Val AI: {count_images(val_ai)} images")
    print(f"  Val Human: {count_images(val_human)} images")

def main():
    parser = argparse.ArgumentParser(description='Download and organize AI vs Human dataset')
    parser.add_argument('--method', choices=['kagglehub', 'manual'], default='kagglehub',
                       help='Download method (default: kagglehub)')
    parser.add_argument('--dataset', type=str, 
                       default='alessandrasala79/ai-vs-human-generated-dataset',
                       help='Kaggle dataset name')
    parser.add_argument('--target_dir', type=str, default='data',
                       help='Target directory for organized dataset')
    parser.add_argument('--organize', action='store_true',
                       help='Automatically organize dataset into train/val structure')
    
    args = parser.parse_args()
    
    if args.method == 'kagglehub':
        download_path = download_via_kagglehub(args.dataset)
        if download_path and args.organize:
            organize_dataset(download_path, args.target_dir)
        elif download_path:
            print(f"\nDataset downloaded to: {download_path}")
            print("To organize it, run with --organize flag")
    else:
        print("For manual download:")
        print("1. Go to: https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset")
        print("2. Click 'Download' button")
        print("3. Extract the zip file")
        print("4. Run this script with --organize and provide the extracted path")

if __name__ == '__main__':
    main()
