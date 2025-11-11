import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

# Common image file extensions
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp'}

def is_image_file(filename):
    """Check if a file is an image based on its extension"""
    return any(filename.lower().endswith(ext) for ext in IMAGE_EXTENSIONS)

class ArtDataset(Dataset):
    def __init__(self, root_dir, split='train', transform=None, class_names=None):
        self.root_dir = os.path.join(root_dir, split)
        self.transform = transform
        self.samples = []
        if class_names is None:
            class_names = sorted([d for d in os.listdir(self.root_dir) if os.path.isdir(os.path.join(self.root_dir, d))])
        self.class_names = class_names
        self.class_to_idx = {c: i for i, c in enumerate(self.class_names)}
        for cls in self.class_names:
            folder = os.path.join(self.root_dir, cls)
            if not os.path.isdir(folder):
                continue
            for name in os.listdir(folder):
                path = os.path.join(folder, name)
                # Only include actual image files, skip .gitkeep and other non-image files
                if os.path.isfile(path) and is_image_file(name):
                    self.samples.append((path, self.class_to_idx[cls]))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        try:
            img = Image.open(path).convert('RGB')
            if self.transform:
                img = self.transform(img)
            return img, label
        except Exception as e:
            # If image is corrupted, try to return a black image or skip
            # For now, we'll raise the error but you could also return a default image
            print(f"Warning: Could not load image {path}: {e}")
            raise

def default_transforms(image_size=224):
    train_tfms = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    val_tfms = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return train_tfms, val_tfms
