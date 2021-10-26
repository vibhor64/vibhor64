import torch
import cv2
from PIL import Image
from yolov5 import detect

detect.run(weights='weights.pt', source='0', device='0', imgsz=640, conf_thres=0.25, project='runs/detect', view_img=True)