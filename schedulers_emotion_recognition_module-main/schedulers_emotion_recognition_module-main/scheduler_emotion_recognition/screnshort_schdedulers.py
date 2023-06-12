from vidgear.gears import ScreenGear
import cv2
import os
from datetime import datetime
import schedule
from trigger_emotions import *
import pyautogui
from collections import Counter
from dotenv import load_dotenv
# open video stream with default parameters
load_dotenv()

def count_emotion(labels):
    emotion_counter = dict(Counter(labels))
    return(emotion_counter)

def clear_directories():

    path=os.getenv('save_directory_screenshot')
    for i in os.listdir(path):
        del_img=os.path.join(path,i)
        os.remove(del_img)
        print("Deleting :", del_img)


def screen_capture_scheduler():
    clear_directories()
    path=os.getenv('save_directory_screenshot')
    current_datetime = datetime.now()

    file_name=str(current_datetime)+".jpg"


    stream = ScreenGear().start()
    screen_captured = stream.read()
    path_save_images=os.path.join(path,file_name)
    print(path_save_images)
    cv2.imwrite(path_save_images,screen_captured)
    stream.stop()

    emotions=trigger_emotion_recognition()
    print(emotions)
    #emotion_counter=count_emotion(emotions)
    #print(emotion_counter)

    #pyautogui.alert(text=emotion_counter, title="Emotion of audience")

def trigger_emotion_Recognition(dict):

    if dict["type"]=="minutes":

        schedule.every(int(dict["value"])).minutes.do(screen_capture_scheduler)
        while True:
            schedule.run_pending()

    if dict["type"]=="seconds":

        schedule.every(int(dict["value"])).seconds.do(screen_capture_scheduler)
        while True:
            schedule.run_pending()

    if dict["type"]=="hour":

        schedule.every(int(dict["value"])).hour.do(screen_capture_scheduler)
        while True:
            schedule.run_pending()
