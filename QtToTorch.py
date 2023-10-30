import torch
from torchvision import transforms, models
import torch.optim as optim


class QtToTorch:
    def __init__(self, model_name, pretrained, device="CPU", **kwargs):
        self.model_name = model_name
        self.pretrained = pretrained
        self.device = device
        self.optimizer = kwargs.pop("optimizer", "SGD")
        self.hyper_params = kwargs

    def load(self):
        """
        Load in the model and the optimizer from the arguments provided by the user"""
        model_attr: models = getattr(models, self.model_name)
        optim_name: optim.Optimizer = getattr(optim, self.optimizer)
        self.model = model_attr(pretrained=self.pretrained)
        self.optimizer = optim_name()

    def preprocess_data(self, dp):
        pass


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
