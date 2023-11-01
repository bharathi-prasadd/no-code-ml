import torch.nn
from torchvision import transforms, models
import torch.optim as optim
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split
import matplotlib.pyplot as plt
from imagewindow import ImageDisp


class QtToTorch:
    def __init__(self, model_name, pretrained, device="CPU", **kwargs):
        self.model_name: str = model_name
        self.pretrained: bool = pretrained
        self.device: str = "cpu" if device == "CPU" else "cuda:0"
        print(self.device)
        self.optimizer: str = kwargs.pop("optimizer", "SGD")
        self.hyper_params = kwargs

    def load_model(self, lr, num_classes) -> None:
        """
        Load in the model and the optimizer from the arguments provided by the user"""
        model_attr: models = getattr(models, self.model_name)
        optim_name: optim.Optimizer = getattr(optim, self.optimizer)
        self.model = model_attr(pretrained=self.pretrained)
        self.model = self.model.to(self.device)
        print(f" Model : {next(self.model.parameters()).device}")
        self.optimizer = optim_name(self.model.parameters(), lr=lr)
        num_ftrs = self.model.fc.in_features
        self.model.fc = torch.nn.Linear(num_ftrs, num_classes)

    def load_data(
        self, train_split: float, batch_size: int, data_path: str
    ) -> [DataLoader, DataLoader]:
        transform = transforms.Compose(
            [
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )
        dataset = datasets.ImageFolder(data_path, transform=transform)
        train_size = int(train_split * len(dataset))
        test_size = len(dataset) - train_size
        train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        return train_loader, test_loader

    def _get_loss(self, num_classes: int):
        if num_classes == 2:
            return torch.nn.BCELoss()
        return torch.nn.CrossEntropyLoss()

    def _dynamic_plot(
        self, train_losses: list[float], train_accuracies: list[float], popup: ImageDisp
    ):
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
        plt.show()

    def _calculate_accuracy(self, outputs, label):
        _, predicted = torch.max(outputs, 1)
        correct = (predicted == label).sum().item()
        total = label.size(0)
        accuracy = correct / total
        return accuracy

    def train(
        self, train_set: DataLoader, num_epochs: int, save_path: str, num_classes: int
    ):
        criterion = self._get_loss(num_classes)
        train_loss = []
        train_acc = []
        plot_interval = 100
        # popup = ImageDisp()
        for epoch in range(num_epochs):
            running_loss = 0
            running_accuracy = 0
            for i, data_point in enumerate(train_set):
                input, label = data_point
                input, label = input.to(self.device), label.to(self.device)
                print(f"input : {input.device}")
                self.optimizer.zero_grad()
                outputs = self.model(input)
                loss = criterion(outputs, label)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()
                running_accuracy += self._calculate_accuracy(outputs, label)

                avg_loss = running_loss / plot_interval
                avg_accuracy = running_accuracy / plot_interval
                train_loss.append(avg_loss)
                train_acc.append(avg_accuracy)
                # self._dynamic_plot(train_loss, train_acc, popup)
                running_loss = 0.0
                running_accuracy = 0.0
            with open("log.txt", "w") as log:
                str = f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}, Accuracy: {avg_accuracy:.4f}"
                print(str)
                log.write(str)
            torch.save(self.model.state_dict(), save_path)


# class ImageNetModelBuilder(ModelBuilder):
#     data_prep = transforms.Compose(
#         [
#             transforms.Resize(256),
#             transforms.CenterCrop(224),
#             transforms.ToTensor(),
#             transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
#         ]
#     )

#     def __init__(self, model_name, pretrained):
#         super().__init__(model_name, pretrained)

#     def load_model(self):
#         return torch.hub.load(
#             "pytorch/vision:v0.10.0", self.model_name, pretrained=self.pretrained
#         )

#     def change_prep(self, pipeline):
#         self.data_prep = pipeline

#     def preprocess_data(self, image):
#         return self.data_prep(image)
