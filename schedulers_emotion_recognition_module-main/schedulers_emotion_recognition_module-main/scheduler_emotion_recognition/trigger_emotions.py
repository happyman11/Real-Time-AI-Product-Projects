from model import *
from face_Detect import *
import os
import numpy
import cv2
from emozise_emotions import *
import csv
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# open the file in the write mode



#'Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral'
def  trigger_emotion_recognition():

    path_test_images=os.getenv('save_directory_screenshot')

    image_list=os.listdir(path_test_images)

    for images in image_list:
        path_images=os.path.join(path_test_images,images)
        image_loaded=cv2.imread(path_images)

        if image_loaded is not None:

            obj_preprocessing=preprocessing(image_loaded)
            face_Rects,image=obj_preprocessing.facenet_pytorch()

            if face_Rects is not None:
                print("yooo")
                MODEL_OBJ=CNNmodel()
                batch_faces=[]
                for x1,y1,x2,y2 in face_Rects:

                    initial_point = (int(x1), int(y1))
                    final_point= (int(x2), int(y2))
                    cropped_images=image_loaded[int(y1):int(y2),int(x1):int(x2)]
                    batch_faces.append(MODEL_OBJ.preprocessmodel(cropped_images))
                    cv2.rectangle(image_loaded,(int(x1), int(y1)),(int(x2), int(y2)),(0,255,255),cv2.FILLED)
                batch_faces=np.asarray(batch_faces)

                labels=MODEL_OBJ.prediction_model(batch_faces)
                #print(labels)


                emojis=emojiemotion(labels)



                return(labels)





















































































































# for x1,y1,x2,y2 in boxes:
#     print(x1,y1,x2,y2)
#     initial_point = (int(x1), int(y1))
#     final_point= (int(x2), int(y2))

#     marked_images=cv2.rectangle(img, initial_point, final_point, (0,0,255),3 )
#     cv2.imwrite("index_marked.jpg", marked_images)




























#img = cv2.imread("/home/transi/Desktop/emotionrecognition/emotionrecognisationpipeline/test_images/index.jpg", cv2.IMREAD_COLOR)
# print(img.shape)
# img=img.astype(np.uint8)
# print(type(img))

# boxes, a = mtcnn.detect(img)
# print(boxes)

# for x1,y1,x2,y2 in boxes:
#     print(x1,y1,x2,y2)
#     initial_point = (int(x1), int(y1))
#     final_point= (int(x2), int(y2))

#     marked_images=cv2.rectangle(img, initial_point, final_point, (0,0,255),3 )
#     cv2.imwrite("index_marked.jpg", marked_images)
