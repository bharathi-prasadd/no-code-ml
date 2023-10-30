#!/usr/bin/env python3
import numpy as np
import pandas as pd

from sklearn.metrics import f1_score  # just for validation


import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np


def dynamic_plot(train_losses, train_accuracies, fig, axes):
    if fig is None or axes is None:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].clear()
    axes[1].clear()

    axes[0].plot(train_losses, label="Training Loss")
    axes[0].set_title("Training Loss")
    axes[0].set_xlabel("Batch")
    axes[0].set_ylabel("Loss")
    axes[0].legend()

    axes[1].plot(train_accuracies, label="Training Accuracy")
    axes[1].set_title("Training Accuracy")
    axes[1].set_xlabel("Batch")
    axes[1].set_ylabel("Accuracy")
    axes[1].legend()

    plt.pause(0.01)
    plt.tight_layout()
    plt.show()


def train_image_classification(model, trainloader, **kwargs):
    defaults = {
        "num_epochs": 10,
        "learning_rate": 0.001,
        "plot_interval": 100,
        "optimizer_name": "SGD",
        "batch_size": 32,
        "data_augmentation": None,
        "weight_initialization": None,
        "regularization": None,
        "learning_rate_schedule": None,
        "loss_function": "CrossEntropy",
        "early_stopping": None,
        "device": "cuda" if torch.cuda.is_available() else "cpu",
        "random_seed": None,
        "gradient_clipping": None,
        "batch_normalization": False,
        "dropout": None,
        "validation_split": 0.2,
        "class_weights": None,
    }

    defaults.update(kwargs)

    num_epochs = defaults["num_epochs"]
    learning_rate = defaults["learning_rate"]
    plot_interval = defaults["plot_interval"]
    optimizer_name = defaults["optimizer_name"]
    batch_size = defaults["batch_size"]
    data_augmentation = defaults["data_augmentation"]
    weight_initialization = defaults["weight_initialization"]
    regularization = defaults["regularization"]
    learning_rate_schedule = defaults["learning_rate_schedule"]
    loss_function = defaults["loss_function"]
    early_stopping = defaults["early_stopping"]
    device = defaults["device"]
    random_seed = defaults["random_seed"]
    gradient_clipping = defaults["gradient_clipping"]
    batch_normalization = defaults["batch_normalization"]
    dropout = defaults["dropout"]
    validation_split = defaults["validation_split"]
    class_weights = defaults["class_weights"]

    if random_seed is not None:
        torch.manual_seed(random_seed)

    model.to(device)

    if loss_function == "CrossEntropy":
        criterion = nn.CrossEntropyLoss(weight=class_weights)

    # Define optimizer
    if optimizer_name == "SGD":
        optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
    elif optimizer_name == "Adam":
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    # Add more options for optimizers as needed

    # Learning rate scheduler
    if learning_rate_schedule == "StepLR":
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)
    # Add more options for learning rate schedules as needed
    fig, axes = None, None

    def calculate_accuracy(outputs, labels):
        _, predicted = torch.max(outputs, 1)
        correct = (predicted == labels).sum().item()
        total = labels.size(0)
        accuracy = correct / total
        return accuracy

    train_losses = []
    train_accuracies = []

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        running_accuracy = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()

            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            running_accuracy += calculate_accuracy(outputs, labels)

            # if i % plot_interval == (plot_interval - 1):
            avg_loss = running_loss / plot_interval
            avg_accuracy = running_accuracy / plot_interval
            train_losses.append(avg_loss)
            train_accuracies.append(avg_accuracy)
            dynamic_plot(train_losses, train_accuracies, fig, axes)
            running_loss = 0.0
            running_accuracy = 0.0

            print(
                f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}, Accuracy: {avg_accuracy:.4f}"
            )

        if learning_rate_schedule is not None:
            scheduler.step()

    print("Training finished!")


# Number of Classes to be taken from the user for optimum training.. through gui or automatically from the image dataset


class ResNet18(nn.Module):
    def __init__(self, num_classes=2):
        super(ResNet18, self).__init__()
        self.resnet18 = models.resnet18(weights=None)
        num_ftrs = self.resnet18.fc.in_features
        self.resnet18.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.resnet18(x)


class VGG16(nn.Module):
    def __init__(self, num_classes=10):
        super(VGG16, self).__init__()
        self.vgg16 = models.vgg16(weights=None)
        num_ftrs = self.vgg16.classifier[6].in_features
        self.vgg16.classifier[6] = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.vgg16(x)


class MobileNetV2(nn.Module):
    def __init__(self, num_classes=10):
        super(MobileNetV2, self).__init__()
        self.mobilenet_v2 = models.mobilenet_v2(weights=None)
        num_ftrs = self.mobilenet_v2.classifier[1].in_features
        self.mobilenet_v2.classifier[1] = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.mobilenet_v2(x)


class DenseNet121(nn.Module):
    def __init__(self, num_classes=10):
        super(DenseNet121, self).__init__()
        self.densenet = models.densenet121(weights=None)  # Load pretrained DenseNet-121

        num_features = self.densenet.classifier.in_features
        self.densenet.classifier = nn.Linear(num_features, num_classes)

    def forward(self, x):
        return self.densenet(x)


transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

dataset = datasets.ImageFolder("/kaggle/input/leukemia-dataset", transform=transform)
train_ratio = 0.66
test_ratio = 1.0 - train_ratio

train_size = int(train_ratio * len(dataset))
test_size = len(dataset) - train_size

train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

batch_size = 32  # Set your desired batch size
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

resnet18 = ResNet18()

vgg16 = VGG16()

mobilenet_v2 = MobileNetV2()

densenet121 = DenseNet121()

densenet121 = models.densenet121(weights=None)

print("resnet18")
train_image_classification(
    resnet18,
    train_loader,
    num_epochs=4,
    learning_rate=0.001,
    optimizer_name="Adam",
    device="cuda:0",
)


save_path = "/kaggle/working/resnet18_trained_model.pth"
torch.save(resnet18.state_dict(), save_path)
print(f"Trained model saved at {save_path}")

# ----------------------------------------------------------------------------------

loaded_model = ResNet18()  # Define the same architecture without pretraining
loaded_model.load_state_dict(torch.load(save_path))
loaded_model.eval()

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def evaluate_model(model, dataloader, device):
    model.eval()
    correct = 0
    total = 0
    all_labels = []
    all_predicted = []

    with torch.no_grad():
        for data in dataloader:
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            model.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            # Convert labels and predictions to numpy arrays
            labels_np = labels.cpu().numpy()
            predicted_np = predicted.cpu().numpy()

            all_labels.extend(labels_np)
            all_predicted.extend(predicted_np)

    accuracy = correct / total
    f1 = f1_score(
        all_labels, all_predicted, average="macro"
    )  # You can use 'micro', 'macro', or 'weighted' for average

    return accuracy, f1


test_accuracy, test_f1_score = evaluate_model(
    loaded_model, test_loader, device="cuda:0"
)
print(f"Test Accuracy: {test_accuracy:.4f}")
print(f"Test F1 Score: {test_f1_score:.4f}")
