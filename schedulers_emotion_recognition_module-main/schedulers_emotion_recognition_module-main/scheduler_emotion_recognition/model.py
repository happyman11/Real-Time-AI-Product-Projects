import tensorflow as tf
import cv2
import numpy as np
from dotenv import load_dotenv
load_dotenv()
import os




class CNNmodel:

    def __init__(self):

        self.class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


        self.path_model=os.getenv('path_model')

    def preprocessmodel(self,image):

        resized_frames=cv2.resize(image, (64,64),interpolation = cv2.INTER_NEAREST)
        resized=cv2.cvtColor(resized_frames, cv2.COLOR_BGR2GRAY)
        ar_frames=np.asarray(resized)
        #print(ar_frames.shape)
        frame=ar_frames.reshape(64,64,1)

        #print(frame.shape)
        return(frame)

    def formatlabels(self,prediction):

        class_index=[np.argmax(probalilities_class) for probalilities_class in prediction]

        class_labels=[self.class_names[i] for i in class_index]

        return(class_labels)


    def prediction_model(self,image):


        model_loaded=tf.keras.models.load_model(self.path_model)
        #model_loaded.summary()
        prediction=model_loaded.predict_on_batch(image)
        #print(prediction)

        class_labels=self.formatlabels(prediction)

        #print(class_labels)

        return(class_labels)
