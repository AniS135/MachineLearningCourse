import cv2
import numpy

def overlay_image_alpha(img, img_overlay, pos, alpha_mask):

    x, y = pos

    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    channels = img.shape[2]

    alpha = alpha_mask[y1o:y2o, x1o:x2o]
    alpha_inv = 1.0 - alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] + alpha_inv * img[y1:y2, x1:x2, c])

#Init Camera
# cv2. VideoCapture(0) . This will return video from the first webcam on your computer.
cap = cv2.VideoCapture(0)

# Face Detection
face_cascade = cv2.CascadeClassifier("Module21SnapchatLikeFilters\\Train\\third-party\\haarcascade_frontalface_alt.xml")

# Eye Detection
eyes_cascade = cv2.CascadeClassifier("Module21SnapchatLikeFilters\\Train\\third-party\\frontalEyes35x16.xml")

# Nose Detection
nose_cascade = cv2.CascadeClassifier("Module21SnapchatLikeFilters\\Train\\third-party\\Nose18x15.xml")

glass = cv2.imread("Module21SnapchatLikeFilters\\Train\\glasses.png", -1)
mustache = cv2.imread("Module21SnapchatLikeFilters\\Train\\mustache.png", -1)

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    eyes = eyes_cascade.detectMultiScale(frame, 1.3, 5)
    eyes = sorted(eyes , key= lambda f : f[2] * f[3], reverse= True)

    for eye in eyes[:1]:
        x, y, w, h = eye
        temGlass = cv2.resize(glass, (w, h))
        overlay_image_alpha(frame, temGlass[:,:,0:3], (x,y), temGlass[:,:,3]/255.0)

    
    noses = nose_cascade.detectMultiScale(frame, 1.3, 5)
    noses = sorted(noses , key= lambda f : f[2] * f[3], reverse= True)

    for nose in noses[:1]:
        x, y, w, h = nose
        temNose = cv2.resize(mustache, (w + w, h))
        h = int(h / 2)
        w = int(w / 2)
        overlay_image_alpha(frame, temNose[:,:,0:3], (x - w, y + h), temNose[:,:,3]/255.0)

    
    cv2.imshow("Frame", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
