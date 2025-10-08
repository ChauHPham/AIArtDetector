import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

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
                if os.path.isfile(path):
                    self.samples.append((path, self.class_to_idx[cls]))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        img = Image.open(path).convert('RGB')
        if self.transform:
            img = self.transform(img)
        return img, label

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
