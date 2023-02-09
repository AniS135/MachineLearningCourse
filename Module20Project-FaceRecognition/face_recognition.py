import cv2
import numpy as np
import os

def dist(x1, x2):
    return np.sqrt(sum((x1 - x2) ** 2))

def knn(train, test, k = 5):
    vals = []
    m = train.shape[0]

    for i in range(m):

        x = train[i, : -1]
        y = train[i, -1]
        d = dist(x, test)
        vals.append((d, y))
    
    vals = sorted(vals, key= lambda x : x[0])
    
    # Nearest/First k points
    vals = vals[:k]

    vals = np.array(vals)

    new_vals = np.unique(vals[:, 1], return_counts= True)
    # print(new_vals)

    index = new_vals[1].argmax()
    pred = new_vals[0][index]

    return pred


#Init Camera
# cv2. VideoCapture(0) . This will return video from the first webcam on your computer.
cap = cv2.VideoCapture(0)

#Face Detection
face_cascade = cv2.CascadeClassifier("Module20Project-FaceRecognition\haarcascade_frontalface_alt.xml")

skip = 0
dataset_path = './Module20Project-FaceRecognition/Data_Stored/'

face_data = []
labels = []

class_id = 0 # Labels for the given file
name = {}

# Data Preperation

for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):

        data_item = np.load(dataset_path + fx)
        face_data.append(data_item)

        # Create Labels for the class
        target = class_id * np.ones((data_item.shape[0], ))
        # Create maping between class_id and name

        name[class_id] = fx[ : -4]
        class_id += 1
        labels.append(target)

face_dataset= np.concatenate(face_data, axis= 0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))

print(face_dataset.shape)
print(face_labels.shape)

trainset = np.concatenate((face_dataset, face_labels), axis= 1)
print(trainset.shape)

# Testing

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    
    for face in faces:
        x, y, w, h = face

        #Get the face ROI
        offset = 10

        face_section = frame[y - offset : y + h + offset , x - offset : x + w + offset]
        face_section = cv2.resize(face_section, (100, 100))

        # Predicted Label (out)
        out = knn(trainset, face_section.flatten())

        # Display on the screen the name and rectangle around it
        pred_name = name[int(out)]
        cv2.putText(frame, pred_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    
    cv2.imshow("Faces", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
