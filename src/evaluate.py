import argparse
import torch
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

from .datasets import ArtDataset, default_transforms
from .model import get_model

def evaluate(args):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    _, val_tfms = default_transforms(args.image_size)
    class_names = ['AI', 'Human'] if args.num_classes == 2 else None
    ds = ArtDataset(args.data_dir, split='val', transform=val_tfms, class_names=class_names)
    loader = DataLoader(ds, batch_size=args.batch_size, shuffle=False, num_workers=4, pin_memory=True)

    model = get_model(num_classes=args.num_classes, pretrained=False).to(device)
    model.load_state_dict(torch.load(args.checkpoint, map_location=device))
    model.eval()

    y_true, y_pred = [], []
    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            logits = model(x)
            y_true.extend(y.numpy().tolist())
            y_pred.extend(logits.argmax(1).cpu().numpy().tolist())

    names = class_names if class_names else [str(i) for i in range(args.num_classes)]
    print(classification_report(y_true, y_pred, target_names=names))
    cm = confusion_matrix(y_true, y_pred)
    plt.imshow(cm, cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted'); plt.ylabel('True')
    plt.xticks(range(len(names)), names, rotation=45)
    plt.yticks(range(len(names)), names)
    for (i, j), v in np.ndenumerate(cm):
        plt.text(j, i, str(v), ha='center', va='center')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--data_dir', type=str, default='data')
    p.add_argument('--checkpoint', type=str, default='models/detector.pth')
    p.add_argument('--batch_size', type=int, default=32)
    p.add_argument('--image_size', type=int, default=224)
    p.add_argument('--num_classes', type=int, default=2)
    args = p.parse_args()
    evaluate(args)
