
import cv2
import numpy as np
from facenet_pytorch import MTCNN
import torch
from dotenv import load_dotenv
load_dotenv()
import os



class preprocessing:


    def __init__ (self,frames,size=(800,800)):


        self.frames = frames

        self.size = size

        self.path_cascade=os.getenv('cascade')

        self.resized_frames=cv2.resize(self.frames,(self.size[0],self.size[1]),interpolation=cv2.INTER_AREA)

    def detect_faces_cascade(self):

        if self.frames is not None:

            Grey_image = cv2.cvtColor(self.resized_frames, cv2.COLOR_BGR2GRAY)

            haar_cascade = cv2.CascadeClassifier(self.path_cascade)

            faces_rect = haar_cascade.detectMultiScale(Grey_image, 1.3, 5)

            # if faces_rect is not None:

            #     for (x, y, w, h) in faces_rect:

            #         cv2.rectangle(self.resized_frames, (x, y), (x + w, y + h), (1, 1, 1), 1)


            return(faces_rect,self.resized_frames)

        else:

            return("None")


    def facenet_pytorch(self):

        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        mtcnn = MTCNN(keep_all=True, device=device)

        img_frames=self.frames.astype(np.uint8)

        boxes, _ = mtcnn.detect( img_frames)


        return(boxes,img_frames)
