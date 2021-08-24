import cv2
import numpy as np
from math import hypot
import time
import FaceMeshModule as fmm
from PIL import Image as im

class FaceFilter():
     def __init__(self, image, dimx, dimy, top, center, left, right, cap):
        self.cap = cap
        self.dimx = int(dimx)
        self.dimy = int(dimy)
        self.ratio = self.dimx/self.dimy
        self.fol = '%.2f'%self.ratio
        self.top = int(top)
        self.center = int(center)
        self.left = int(left)
        self.right = int(right)
        self.image = image
        self.success, self.frame = self.cap.read()
        
        self.detector = fmm.FaceMeshDetector()
        self.img, self.faces = self.detector.findFaceMesh(self.frame, draw=False)
        self.data = np.array_str(self.image)
        self.new_image = cv2.imread(self.data)
        self.rows, self.cols, _ = self.frame.shape
        self.object_mask = np.zeros((self.rows, self.cols), np.uint8)
        self.object_mask.fill(0)
        self.gray_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        if len(self.faces) != 0:

            self.top_object = self.faces[self.top]
            self.center_object = self.faces[self.center]
            self.left_object = self.faces[self.left]
            self.right_object = self.faces[self.right]



            self.object_width = int(hypot(self.left_object[0] - self.right_object[0],
                               self.left_object[1] - self.right_object[1]) * 1.3)
            self.object_height = int(self.object_width * self.ratio)

            # New object position
            self.top_left = (int(self.center_object[0] - self.object_width / 2),
                                  int(self.center_object[1] - self.object_height / 2))
            self.bottom_right = (int(self.center_object[0] + self.object_width / 2),
                           int(self.center_object[1] + self.object_height / 2))


            # Adding the new object
            self.object_catg = cv2.resize(self.image, (self.object_width, self.object_height))
            self.object_catg_gray = cv2.cvtColor(self.object_catg, cv2.COLOR_BGR2GRAY)
            _, self.object_mask = cv2.threshold(self.object_catg_gray, 25, 255, cv2.THRESH_BINARY_INV)

            self.object_area = self.frame[self.top_left[1]: self.top_left[1] + self.object_height,
                        self.top_left[0]: self.top_left[0] + self.object_width]
            self.object_area_no_object = cv2.bitwise_and(self.object_area, self.object_area, mask=self.object_mask)
            self.final_object = cv2.add(self.object_area_no_object, self.object_catg)

            self.frame[self.top_left[1]: self.top_left[1] + self.object_height,
                        self.top_left[0]: self.top_left[0] + self.object_width] = self.final_object

            # cv2.imshow("object area", object_area)
            # cv2.imshow("object catg", object_catg)
            # cv2.imshow("final object", final_object)
        cv2.imshow("Frame", self.frame)
        


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = fmm.FaceMeshDetector()
    pig_nose = cv2.imread("pig_nose.png")
    while True:
        success, frame = cap.read()
        img, faces = detector.findFaceMesh(frame, draw=False)
        FaceFilter(pig_nose, 400, 400, 195, 4, 64, 278, cap)
        # rows, cols, _ = frame.shape
        # object_mask = np.zeros((rows, cols), np.uint8)
        # object_mask.fill(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        


if __name__ == "__main__":
    main()