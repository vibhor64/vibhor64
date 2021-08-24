import cv2 
import time
import FaceFilterModule as ffm
import FaceMeshModule as fmm

cap = cv2.VideoCapture(0)
pTime = 0
detector = fmm.FaceMeshDetector()
pig_nose = cv2.imread("pig_nose1.png")
while True:
        success, frame = cap.read()
        img, faces = detector.findFaceMesh(frame, draw=False)
        ffm.FaceFilter(pig_nose, 400, 400, 195, 4, 64, 278, cap)
        # rows, cols, _ = frame.shape
        # object_mask = np.zeros((rows, cols), np.uint8)
        # object_mask.fill(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break