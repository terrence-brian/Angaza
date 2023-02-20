import cv2
import os
import time
import uuid

img_path = 'Tensorflow/workspace/images/collectedimages'

labels = ['KSL-G', 'KSL-I']
img_num = 16

for label in labels:
  !mkdir {'Tensorflow\workspace\images\collectedimages\\'+label}
  cap = cv2.VideoCapture(0)
  print('Collecting images for {}'.format(label))
  time.sleep(5)
  for imgnum in range(img_num):
    ret, frame = cap.read()
    imgname = os.path.join(img_path, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(2)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
      break
  
  cap.release()

cap.release()

cv2.destroyAllWindows()

