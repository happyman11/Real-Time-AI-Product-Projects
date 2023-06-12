
import os
import json
import environ
from os.path import join
from os.path import exists
from os.path import dirname
from twilio.rest import Client



class Dishpatcher_sms():
    
    """
    Class_Description:
    
         This class is dedicated to send the message to users
         based of the prediction i.e. recommendation of the courses.
         The message is send to the user who are inactive.

    
    
       
    Extracted from the .env file

        twilio credentials: 
   

                account_sid :
                             type: <String>
                auth_token : 
                             type: <String>
                Phn_no_twillio: 
                             type: <String>  
                watsapptwillio:
                             type: <String>         
                             


                              
    Functions:
    
           Decsription: This classimplements two function which are
           
                       1. send_sms_twillio():
                          
                                          Descriptions: It sends the message to the user using twillow account account.

                          Args:
        
                                reciever_number :
                                                    type:<String>
                                                    Description: User Number in the format **********

                                message:
                                                    type:<String>
                                                    Description: As per the  enduser choice

                       2. send_watsappsms_twillio():
                          
                                          Descriptions: It sends the message to the user watsapp using twillow watsapp account.  
                                          
                          Args:
        
                                reciever_number :
                                                    type:<String>
                                                    Description: User Number in the format **********

                                message:
                                                    type:<String>
                                                    Description: As per the  enduser choice

    """

    def __init__(self):
       
       
       
        """
        Constructor of the Dishpatcher_sms used to
        initialise the variables.

        """

        #for environment file

        env                     =       environ.Env()
        environ.Env.read_env()
        env_file                =       join(dirname(__file__), '.env')


        #for twillio credentials .env file
       
        
        self.account_sid        =       env('Account_SSID')
        self.auth_token         =       env('Auth_token')
        self.Phn_no_twillio     =       env('Phn_no_twillio')


        # for watsaopp

        self.watsapptwillio     =       env('Phn_no_twilliowatsapp')


    def send_sms_twillio(self,message,reciever_number_twillio):

      """
      Description:
                Function: which sends message from the twilio account.
               
      
      """
            
      client_object             =       Client(self.account_sid, self.auth_token)
          
            
      try:
          sms                   =       client_object.messages.create(
                                                                        body    =message,
                                                                        from_   =self.Phn_no_twillio,
                                                                        to      =reciever_number_twillio 
                                                                    )
        

          dev                   =       {}
          dev["response"]       =       "Message Sent Sucessfully"
          dev["sms.sid"]        =       sms.sid
          dev["Provided By:"]   =       "Chadura Communication Api Services"
          dev["status"]         =       200
          
          return(dev)
          
                                 
      except:
                
          dev                   =       {}
          dev["response"]       =       "Message Sending Failed"
          dev["sms.sid"]        =       "Null"
          dev["Provided By:"]   =       "Chadura Communication Api Services"
          dev["status"]         =       404

          return(dev)


    def send_watsappsms_twillio(self,message,reciever_number_twillio):

      """
      Description:
                Function: which sends message from the twilio Facebooaccount.
               
      
      """
            
      client_object             =       Client(self.account_sid, self.auth_token)

      watsapp_client            =       "whatsapp:"+reciever_number_twillio
            
      try:
          sms= client_object.messages.create(
                                           body=message,
                                           from_=self.watsapptwillio,
                                           to=watsapp_client
                                           )
           
          print(sms)
          dev = {}
          dev["response"]       =       "Message Sent Sucessfully"
          dev["sms.sid"]        =       sms.sid
          dev["Provided By:"]   =       "Chadura Communication Api Services"
          dev["status"]         =       200
          
          return(dev)
          
                                 
      except:
                
          dev = {}
          dev["response"]       =       "Message Sending Failed"
          dev["sms.sid"]        =       "Null"
          dev["Provided By:"]   =       "Chadura Communication Api Services"
          dev["status"]         =       404

          return(dev)

    
    def call_twilio(self,message,reciever_number_twillio):

      """
      Description:
                Function: which sends message from the twilio Facebooaccount.
               
      
      """
            
      client_object             =       Client(self.account_sid, self.auth_token)
      
      first_message             =       "<Response><Say>"
      last_message              =       "</Say></Response>"
      callmessage               =       first_message+message+last_message
      try:
          call=client_object.calls.create(
                                            from_   =   self.Phn_no_twillio,
                                            to      =   str(reciever_number_twillio),
                                            twiml   =   callmessage

                                        )
           
          print(call)
          dev                   =       {}
          dev["response"]       =       "Message Sent Sucessfully"
          dev["call.sid"]       =       call.sid
          dev["Provided By:"]   =       "Chadura Communication Api Services"
          dev["status"]         =       200
          
          return(dev)
          
                                 
      except:
                
          dev = {}
          dev["response"]       =       "Message Sending Failed"
          dev["call.sid"]       =       "Null"
          dev["Provided By:"]   =       "Chadura Communication Api Services"
          dev["status"]         =       404

          return(dev)


        



