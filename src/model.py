import torch.nn as nn
from torchvision import models

def get_model(num_classes=3, pretrained=True):
    model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT if pretrained else None)
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)
    return model
