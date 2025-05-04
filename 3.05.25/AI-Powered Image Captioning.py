import torch
from torchvision import models, transforms
from PIL import Image

model = models.resnet50(pretrained=True)
model.eval()

image = Image.open("sample.jpg")
transform = transforms.Compose([transforms.Resize(256), transforms.ToTensor()])
image_tensor = transform(image).unsqueeze(0)

output = model(image_tensor)
print("Generated Caption:", output.argmax().item())
