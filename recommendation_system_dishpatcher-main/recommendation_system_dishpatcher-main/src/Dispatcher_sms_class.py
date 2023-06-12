from twilio.rest import Client
from logging_class import *
import requests
import environ
import json
import os


class Dishpatcher_sms():
    """
    Class_Description:
    
         This class is dedicated to send the message to users
         based of the prediction i.e. recommendation of the courses.
         The message is send to the user who are inactive.

    
    Args:
        
        reciever_number :
                         type:<String>
                        Description: User Number in the format **********

        message:
                type:<String>
                Description: REcommended Courses to then User
       
        Extracted from the .env file

        twilio credentials: 
   

                account_sid :
                             type: <String>
                auth_token : 
                             type: <String>
                Phn_no_twillio: 
                             type: <String>    
                             
        Fast2SMS credentials: 
   

                fast2sms_url :
                             type: <String>
                fast2sms_apikey : 
                             type: <String>
                sender_id_fast2sms: 
                             type: <String>    
                             
                             
    Functions:
    
           Decsription: This classimplements two function which are
           
                       1. send_sms_twillio():
                          
                                          Descriptions: It sends the message to the user using twillow account account.  
                                          
                       2. send_sms_Fast2SMS():     
                         
                                          Descriptions: It sends the message to the user using Fast2SMS Api account .      

    """
         
    def __init__(self,reciever_number,message):
       
       
       
        """
        Constructor of the Dishpatcher_sms used to
        initialise the variables.

        """
        
        
       
        
        #Reading the .env file
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        File_Path = BASE_DIR +"/.env"
        
        env = environ.Env()
        environ.Env.read_env(File_Path)
        
        #for twillio credentials .env file
        self.reciever_number_twillio = "+9191"+reciever_number
        self.message = message
        self.account_sid = env('Account_SSID')
        self.auth_token =env('Auth_token')
        self.Phn_no_twillio=env('Phn_no_twillio')
        
        
        #for Fast2sms api
        self.reciever_number_fast2api=reciever_number
        self.fast2sms_apikey=env('apikey_fastapi')
        self.fast2sms_url=env('fast_api_url')
        self.sender_id_fast2sms=env('fast2sms_Sender_id')
        self.Content_Type=env('Content_Type')
        self.Cache_Control=env('Cache_Control')
        self.language_sms=env('language_sms')
        self.route_sms=env('routing')
         
        
            
    def send_sms_twillio(self):

      """
      Description:
                Function: which sends message from the twilio account.
               
      
      """
            
      client_object = Client(self.account_sid, self.auth_token)
          
            
      try:
          sms= client_object.messages.create(
                                           body=self.message,
                                           from_=self.Phn_no_twillio,
                                           to=self.reciever_number_twillio 
                                           )
          print(sms.sid)
          
          msg="SMS-Dishpatcher-class >> Function - send_sms_twillio: message sent successfully, id:"+sms.sid+" number :" + str(self.reciever_number_twillio)
          obj_logging = logging_information(msg)
          obj_logging.Logger_function_critical()
          #print(msg) 
          
                                 
      except:
                
          
          msg="SMS-Dishpatcher-class >> Function - send_sms_twillio: message sending failed" + " number :" +str(self.reciever_number_twillio)
          obj_logging = logging_information(msg)
          obj_logging.Logger_function_critical()
          #print(msg)
          
          
          
          
    def send_sms_Fast2SMS(self):
    
      """
      Description:
                Function: which sends message from the account using Fast2sms.
               
      
      """

      
     
      payload= {'sender_id': self.sender_id_fast2sms, 
                 'message': self.message, 
                'language': self.language_sms,
                'route': self.route_sms,
                 'numbers': self.reciever_number_fast2api
                }
    
    
      headers = {
                'authorization': self.fast2sms_apikey,
                'Content-Type': self.Content_Type,
                'Cache-Control': self.Cache_Control
               }

          
            
      try:
          response = requests.request("POST",
                                      self.fast2sms_url,
                                      data = payload,
                                      headers = headers)
          
          returned_msg = json.loads(response.text)

          
        
          
          if (str(returned_msg['return']) == 'True'):
              
              msg="SMS-Dishpatcher-class >> Function - send_sms_Fast2SMS :"+str(returned_msg['message'])+" id:"+str(returned_msg['request_id'])+" number :" +str(self.reciever_number_fast2api)
              obj_logging = logging_information(msg)
              obj_logging.Logger_function_critical()
              #print(returned_msg)
            
          else:
              
              msg="SMS-Dishpatcher-class >> Function - send_sms_Fast2SMS :"+str(returned_msg['message'])+" id:"+str(returned_msg['request_id'])+ " number :" +str(self.reciever_number_fast2api)
              obj_logging = logging_information(msg)
              obj_logging.Logger_function_critical()
              #print(returned_msg)
           
               
      except:
          
          msg="SMS-Dishpatcher-class >> Function - send_sms_Fast2SMS : Exception occured check credentials"+ " number :" +str(self.reciever_number_fast2api)
          obj_logging = logging_information(msg)
          obj_logging.Logger_function_critical()
          #print(returned_msg)
                                 
     
                       