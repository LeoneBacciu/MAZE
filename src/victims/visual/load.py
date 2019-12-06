from utils.recorder import Camera
import cv2
from json import loads

cam = Camera(0)

json = open('config.json', 'r').read()
data = loads(json)
data = data['loading']
print(data)
directory = data['directory']
class_ = data['class']
samples = data['total_samples']


def save(i, frame):
    print(i)
    if i < (samples // 3) * 2:
        cv2.imwrite(directory + '/train/' + class_ + '/' + str(i) + '.png', frame)
    else:
        cv2.imwrite(directory + '/pred/' + class_ + '/' + str(i - 1000) + '.png', frame)


cam.record(save, samples)
