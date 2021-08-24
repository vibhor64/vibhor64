import cv2
import numpy as np


with open('object_detection_classes_coco.txt', 'r') as f:
    class_names = f.read().split('\n')


# get a different color array for each of the classes:
# We have a COLORS array that holds tuples of three integer values. These are random 
# colors that we can apply while drawing the bounding box for each class. The best part is that we will have a 
# different colored bounding box for each class, and it will be quite easy for us to differentiate between the 
# classes in the final result. 
COLORS = np.random.uniform(0, 255, size=(len(class_names), 3))

model = cv2.dnn.readNet(model='frozen_inference_graph.pb', # a pre-trained model that contains the weights.
                        config='ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt', 
                        framework='TensorFlow')


image = cv2.imread('image_2.jpg')
image_height, image_width, _ = image.shape

blob = cv2.dnn.blobFromImage(image=image, size=(300, 300), mean=(104, 117, 123), 
                             swapRB=True) # BGR2RGB
# mean: The mean argument is pretty important. These are actually the mean values that are subtracted 
# from the image’s RGB color channels. This normalizes the input and makes the final input invariance to 
# different illumination scales.


model.setInput(blob)
output = model.forward()

# loop over each of the detection
for detection in output[0, 0, :, :]:
    # extract the confidence of the detection
    confidence = detection[2]
    # draw bounding boxes only if the detection confidence is above...
    # ... a certain threshold, else skip
    # print(confidence)
    if confidence > .4:
        # get the class id
        class_id = detection[1]
        # map the class id to the class
        class_name = class_names[int(class_id)-1]
        color = COLORS[int(class_id)]
        # get the bounding box coordinates
        box_x = detection[3] * image_width
        box_y = detection[4] * image_height
        # get the bounding box width and height
        box_width = detection[5] * image_width
        box_height = detection[6] * image_height
        # draw a rectangle around each detected object
        cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=2)
        # put the FPS text on top of the frame
        cv2.putText(image, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

cv2.imshow('image', image)
cv2.imwrite('../../outputs/image_result.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
