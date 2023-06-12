

###SMS checking
from Dispatcher_sms_class import *



reciever="8676853586"
msg_sms="hi testing msg from sms"
cms_object=Dishpatcher_sms(reciever,msg_sms)
cms_object.send_sms_Fast2SMS()
cms_object.send_sms_twillio() 





#email checking

from Dispatcher_email_class import *
reciever_email="tiwari11.rst@gmail.com"
subject="Hi testing mail"
message="yooooo"
object_email=Dishpatcher_email(reciever_email,subject,message)
object_email.send_email()


# reading .env file
"""
import os 
import environ
env = environ.Env()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR1 = BASE_DIR +"/.env"

print("BASE_DIR1:::::::",BASE_DIR1)
#environ.Env.read_env(os.File "/usr/lib64/python3.10/logging/__init__.py", line 2040, in basicConfig
    h = FileHandler(filename, mode,
  File "/usr/lib64/python3.10/logging/__init__.py", line 1169, in __init__
    StreamHandler.__init__(self, self._open())
  File "/usr/lib64/python3.10/logging/__init__.py", line 1201, in _open
    return open_func(self.baseFilename, self.mode,


SECRET_KEY = env('Auth_token')
print(SECRET_KEY)


print(env('smtp_server'))
print(env('port'))
print(env('account_host'))
print((env('app_password')))

print(type(env('smtp_server')))
print(type(env('port')))
print(type(env('account_host')))
print((type(env('app_password'))))
print(type(int(env('port'))))
"""

"""
import logging
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_file=File_Path = BASE_DIR +'/logs/app.log'

logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
logging.warning('This will get logged to a file')
logging.info('This will get logged to a file')
"""

"""
from logging_class import *

obj_log=logging_information("test")
obj_log.Logger_function_info()

obj_log=logging_information("test1")
obj_log.Logger_function_warning()

obj_log=logging_information("test2")
obj_log.Logger_function_critical()
"""