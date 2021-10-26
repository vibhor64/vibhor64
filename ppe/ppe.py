import torch
import cv2
from PIL import Image

model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights.pt')

img = cv2.imread('mask.png')[:,:,::-1] 

# model.conf = 0.25
results = model(img, size =640)
results.print()
results.save()
results.show()