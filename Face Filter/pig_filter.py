import cv2
import numpy as np
from math import hypot
import FaceMeshModule as fmm

# Loading Camera and Nose image and Creating mask
cap = cv2.VideoCapture(0)
nose_image = cv2.imread("pig_nose.png")
# cv2.imshow("nose_image", nose_image)
success, frame = cap.read()
rows, cols, _ = frame.shape
nose_mask = np.zeros((rows, cols), np.uint8)

# Loading Face detector
detector = fmm.FaceMeshDetector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    success, frame = cap.read()
    img, faces = detector.findFaceMesh(frame, draw=False)
    nose_mask.fill(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(faces[0])
    # Nose coordinates
    # cv2.circle(frame, faces[278], 5, color = (0, 255, 0), thickness=10)
    if len(faces) != 0:
        top_nose = faces[195]
        center_nose = faces[4]
        left_nose = faces[64]
        right_nose = faces[278]
    
    
        nose_width = int(hypot(left_nose[0] - right_nose[0],
                           left_nose[1] - right_nose[1]) * 1.3)
        nose_height = int(nose_width * 1)
        
        # New nose position
        top_left = (int(center_nose[0] - nose_width / 2),
                              int(center_nose[1] - nose_height / 2))
        bottom_right = (int(center_nose[0] + nose_width / 2),
                       int(center_nose[1] + nose_height / 2))
    
    
        # Adding the new nose
        nose_pig = cv2.resize(nose_image, (nose_width, nose_height))
        nose_pig_gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
        _, nose_mask = cv2.threshold(nose_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)
        
        nose_area = frame[top_left[1]: top_left[1] + nose_height,
                    top_left[0]: top_left[0] + nose_width]
        nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
        final_nose = cv2.add(nose_area_no_nose, nose_pig)
        
        frame[top_left[1]: top_left[1] + nose_height,
                    top_left[0]: top_left[0] + nose_width] = final_nose
    
        # cv2.imshow("Nose area", nose_area)
        # cv2.imshow("Nose pig", nose_pig)
        # cv2.imshow("final nose", final_nose)


    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break