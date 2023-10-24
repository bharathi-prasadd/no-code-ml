#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[ ]:


import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np

def dynamic_plot(train_losses, train_accuracies):
    plt.figure(figsize=(12, 4))
    plt.subplot(121)
    plt.plot(train_losses, label="Training Loss")
    plt.title("Training Loss")
    plt.xlabel("Batch")
    plt.ylabel("Loss")
    plt.legend()
    plt.subplot(122)
    plt.plot(train_accuracies, label="Training Accuracy")
    plt.title("Training Accuracy")
    plt.xlabel("Batch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.tight_layout()
    display(plt.show())


def train_image_classification(model, trainloader, **kwargs):
    defaults = {
        'num_epochs': 10,
        'learning_rate': 0.001,
        'plot_interval':100,
        'optimizer_name': "SGD",
        'batch_size': 32,
        'data_augmentation': None,
        'weight_initialization': None,
        'regularization': None,
        'learning_rate_schedule': None,
        'loss_function': "CrossEntropy",
        'early_stopping': None,
        'device': "cuda" if torch.cuda.is_available() else "cpu",
        'random_seed': None,
        'gradient_clipping': None,
        'batch_normalization': False,
        'dropout': None,
        'validation_split': 0.2,
        'class_weights': None
    }

    defaults.update(kwargs)
    
    num_epochs = defaults['num_epochs']
    learning_rate = defaults['learning_rate']
    plot_interval = defaults['plot_interval']
    optimizer_name = defaults['optimizer_name']
    batch_size = defaults['batch_size']
    data_augmentation = defaults['data_augmentation']
    weight_initialization = defaults['weight_initialization']
    regularization = defaults['regularization']
    learning_rate_schedule = defaults['learning_rate_schedule']
    loss_function = defaults['loss_function']
    early_stopping = defaults['early_stopping']
    device = defaults['device']
    random_seed = defaults['random_seed']
    gradient_clipping = defaults['gradient_clipping']
    batch_normalization = defaults['batch_normalization']
    dropout = defaults['dropout']
    validation_split = defaults['validation_split']
    class_weights = defaults['class_weights'] 
    
    if random_seed is not None:
        torch.manual_seed(random_seed)
    
    model.to(device)

    if loss_function == "CrossEntropy":
        criterion = nn.CrossEntropyLoss(weight=class_weights)
    
    if optimizer_name == "SGD":
        optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
    elif optimizer_name == "Adam":
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    if learning_rate_schedule == "StepLR":
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)
    # Add more options for learning rate schedules as needed
    
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

            if i % plot_interval == (plot_interval - 1):
                avg_loss = running_loss / plot_interval
                avg_accuracy = running_accuracy / plot_interval
                train_losses.append(avg_loss)
                train_accuracies.append(avg_accuracy)
                
                dynamic_plot(train_losses, train_accuracies)
                
                running_loss = 0.0
                running_accuracy = 0.0
        
                print(f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}, Accuracy: {avg_accuracy:.4f}")

        if learning_rate_schedule is not None:
            scheduler.step()

    print("Training finished!")



# In[1]:


import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split
import torchvision.datasets as datasets
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim


def train_image_classification(model, trainloader, **kwargs):
    defaults = {
        'num_epochs': 10,
        'learning_rate': 0.001,
        'optimizer_name': "SGD",
        'batch_size': 32,
        'data_augmentation': None,
        'weight_initialization': None,
        'regularization': None,
        'learning_rate_schedule': None,
        'loss_function': "CrossEntropy",
        'early_stopping': None,
        'device': "cuda:0" if torch.cuda.is_available() else "cpu",
        'random_seed': None,
        'gradient_clipping': None,
        'batch_normalization': False,
        'dropout': None,
        'validation_split': 0.2,
        'class_weights': None
    }

    defaults.update(kwargs)
    
    num_epochs = defaults['num_epochs']
    learning_rate = defaults['learning_rate']
    optimizer_name = defaults['optimizer_name']
    batch_size = defaults['batch_size']
    data_augmentation = defaults['data_augmentation']
    weight_initialization = defaults['weight_initialization']
    regularization = defaults['regularization']
    learning_rate_schedule = defaults['learning_rate_schedule']
    loss_function = defaults['loss_function']
    early_stopping = defaults['early_stopping']
    device = defaults['device']
    random_seed = defaults['random_seed']
    gradient_clipping = defaults['gradient_clipping']
    batch_normalization = defaults['batch_normalization']
    dropout = defaults['dropout']
    validation_split = defaults['validation_split']
    class_weights = defaults['class_weights'] 

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
    
    # Training loop
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            #for batch in trainloader:
            #inputs, labels = batch
            inputs = inputs.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # Backpropagation and optimization
            loss.backward()
            
            # Gradient clipping (if specified)
            if gradient_clipping is not None:
                torch.nn.utils.clip_grad_norm_(model.parameters(), gradient_clipping)
            
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch {epoch + 1}, Loss: {running_loss / len(trainloader)}")
        
        # Learning rate scheduling (if specified)
        if learning_rate_schedule is not None:
            scheduler.step()

    print("Training finished!")


# In[2]:


class ResNet18(nn.Module):
    def __init__(self, num_classes=2):
        super(ResNet18, self).__init__()
        self.resnet18 = models.resnet18(weights=None)
        num_ftrs = self.resnet18.fc.in_features
        self.resnet18.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.resnet18(x)


# In[ ]:


class VGG16(nn.Module):
    def __init__(self, num_classes=10):
        super(VGG16, self).__init__()
        self.vgg16 = models.vgg16(weights=None)
        num_ftrs = self.vgg16.classifier[6].in_features
        self.vgg16.classifier[6] = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.vgg16(x)


# In[ ]:


class MobileNetV2(nn.Module):
    def __init__(self, num_classes=10):
        super(MobileNetV2, self).__init__()
        self.mobilenet_v2 = models.mobilenet_v2(weights=None)
        num_ftrs = self.mobilenet_v2.classifier[1].in_features
        self.mobilenet_v2.classifier[1] = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.mobilenet_v2(x)


# In[ ]:


class DenseNet121(nn.Module):
    def __init__(self, num_classes=10):
        super(DenseNet121, self).__init__()
        self.densenet = models.densenet121(weights=None)  # Load pretrained DenseNet-121

        num_features = self.densenet.classifier.in_features
        self.densenet.classifier = nn.Linear(num_features, num_classes)

    def forward(self, x):
        return self.densenet(x)


# In[3]:


transform = transforms.Compose([
                                transforms.Resize(256),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                            ])


# In[4]:


dataset = datasets.ImageFolder('/kaggle/input/leukemia-dataset', transform=transform)
#dataset = datasets.ImageFolder('/kaggle/input/multidimensional-choledoch-database', transform=transform)
train_ratio = 0.66
test_ratio = 1.0 - train_ratio

train_size = int(train_ratio * len(dataset))
test_size = len(dataset) - train_size

train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

batch_size = 32  # Set your desired batch size
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


# In[ ]:


#trainloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)


# In[5]:


resnet18 = ResNet18()


# In[ ]:


vgg16 = VGG16()


# In[ ]:


mobilenet_v2 = MobileNetV2()


# In[ ]:


densenet121 = DenseNet121()


# In[6]:


print('resnet18')
train_image_classification(resnet18, train_loader, num_epochs=12, learning_rate=0.001, optimizer_name="Adam",device='cuda:0')


# In[ ]:


print('vgg16')
train_image_classification(vgg16, train_loader, num_epochs=12, learning_rate=0.001, optimizer_name="Adam",device='cuda:0')


# In[ ]:


print('mobilenet_v2')
train_image_classification(mobilenet_v2, train_loader, num_epochs=12, learning_rate=0.001, optimizer_name="Adam",device='cuda:0')


# In[ ]:


print('densenet121')
train_image_classification(densenet121, train_loader, num_epochs=12, learning_rate=0.001, optimizer_name="Adam",device='cuda:0')


# In[ ]:


#testloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)


# In[ ]:


import torch
import numpy as np
from sklearn.metrics import f1_score

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
    f1 = f1_score(all_labels, all_predicted, average='macro')  # You can use 'micro', 'macro', or 'weighted' for average
    
    return accuracy, f1


# In[ ]:


test_accuracy, test_f1_score = evaluate_model(resnet18, test_loader, device='cuda:0')
print(f"Test Accuracy: {test_accuracy:.4f}")
print(f"Test F1 Score: {test_f1_score:.4f}")


# In[ ]:


test_accuracy, test_f1_score = evaluate_model(vgg16, test_loader, device='cuda:0')
print(f"Test Accuracy: {test_accuracy:.4f}")
print(f"Test F1 Score: {test_f1_score:.4f}")


# In[ ]:

test_accuracy, test_f1_score = evaluate_model(mobilenet_v2, test_loader, device='cuda:0')
print(f"Test Accuracy: {test_accuracy:.4f}")
print(f"Test F1 Score: {test_f1_score:.4f}")


# In[ ]:

test_accuracy, test_f1_score = evaluate_model(densenet121, test_loader, device='cuda:0')
print(f"Test Accuracy: {test_accuracy:.4f}")
print(f"Test F1 Score: {test_f1_score:.4f}")
