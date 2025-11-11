import os
import argparse
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

from .datasets import ArtDataset, default_transforms
from .model import get_model

def train(args):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    class_names = ['AI', 'Human'] if args.num_classes == 2 else None
    train_tfms, val_tfms = default_transforms(args.image_size)

    train_ds = ArtDataset(args.data_dir, split='train', transform=train_tfms, class_names=class_names)
    val_ds = ArtDataset(args.data_dir, split='val', transform=val_tfms, class_names=class_names)

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, num_workers=4, pin_memory=True)

    model = get_model(num_classes=args.num_classes, pretrained=not args.no_pretrain).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)

    best_acc = 0.0
    os.makedirs(os.path.dirname(args.checkpoint), exist_ok=True)

    for epoch in range(args.epochs):
        model.train()
        running_loss, running_corrects = 0.0, 0
        for x, y in tqdm(train_loader, desc=f"Train {epoch+1}/{args.epochs}"):
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * x.size(0)
            running_corrects += (logits.argmax(1) == y).sum().item()
        train_loss = running_loss / len(train_ds)
        train_acc = running_corrects / len(train_ds)

        # eval
        model.eval()
        val_corrects, val_loss_sum = 0, 0.0
        with torch.no_grad():
            for x, y in tqdm(val_loader, desc="Val"):
                x, y = x.to(device), y.to(device)
                logits = model(x)
                loss = criterion(logits, y)
                val_loss_sum += loss.item() * x.size(0)
                val_corrects += (logits.argmax(1) == y).sum().item()
        val_loss = val_loss_sum / len(val_ds)
        val_acc = val_corrects / len(val_ds)
        print(f"Epoch {epoch+1}: train_loss={train_loss:.4f} acc={train_acc:.4f} | val_loss={val_loss:.4f} acc={val_acc:.4f}")

        if val_acc > best_acc:
            best_acc = val_acc
            torch.save(model.state_dict(), args.checkpoint)
            print("Saved best model ->", args.checkpoint)

    print("Best val acc:", best_acc)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--data_dir', type=str, default='data')
    p.add_argument('--checkpoint', type=str, default='models/detector.pth')
    p.add_argument('--epochs', type=int, default=10)
    p.add_argument('--batch_size', type=int, default=32)
    p.add_argument('--lr', type=float, default=1e-4)
    p.add_argument('--image_size', type=int, default=224)
    p.add_argument('--num_classes', type=int, default=2)
    p.add_argument('--no_pretrain', action='store_true')
    args = p.parse_args()
    train(args)
