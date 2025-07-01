import cv2 as cv

#Capture image
#img=cv.imread("photos/imga.jpg")

#Load image in a window
#cv.imshow('Stolen Pic',img)

#Define number of times to wait for a key to be pressed
#cv.waitKey(0)

#Reading Videos
video=cv.VideoCapture("videos/another.mp4")
while True:
    isTrue,frame=video.read()
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()
cv.waitKey(0)