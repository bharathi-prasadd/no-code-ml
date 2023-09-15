import torch
from torchvision import transforms

class ModelBuilder:

    def __init__(self,model_name,pretrained):
        self.pretrained = pretrained
        self.model_name = model_name

    def load_model(self):
       pass
    def preprocess_data(self,dp):
        pass

class ImageNetModelBuilder(ModelBuilder):

    data_prep = transforms.Compose([
                                transforms.Resize(256),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                            ])

    def __init__(self,model_name,pretrained):
        super().__init__(model_name,pretrained)

    def load_model(self):
        return torch.hub.load('pytorch/vision:v0.10.0',self.model_name,pretrained = self.pretrained)

    def change_prep(self,pipeline):
        self.data_prep = pipeline

    def preprocess_data(self,image):
        return self.data_prep(image)
