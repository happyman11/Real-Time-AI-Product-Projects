
import os
import re
import environ
from os.path import join
from os.path import exists
from os.path import dirname
from xml.dom import minidom
from bs4 import BeautifulSoup
from django.conf import settings


def read_xml(tags,path):

    path    =  str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        
    with open(path, 'r') as f:
        data = f.read()
        
    Bs_data  =  BeautifulSoup(data, "xml")
    b_unique =  Bs_data.find(tags)
    word   =  str(b_unique.contents[0]).strip()

    return(word)
