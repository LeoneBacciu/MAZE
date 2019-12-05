import cv2
import numpy as np
import tifffile
from utils import recorder

cam = recorder.Camera(2)
def f(frame):
    d = frame.astype(np.float32) / 255
    tifffile.imwrite('f.tif', d)

# cam.record(f, 1)
cv2.imshow('f', cv2.imread('f.tif'))
while True:
    pass
