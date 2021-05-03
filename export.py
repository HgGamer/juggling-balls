import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('source/video.mp4')
success,image = vidcap.read()
count = 0
while success:
  ##image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
  cv2.imwrite("export/frame%d.png" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1