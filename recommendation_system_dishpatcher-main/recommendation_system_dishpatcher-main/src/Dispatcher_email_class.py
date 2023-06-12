from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from logging_class import *
import  random as r
import environ
import smtplib
import time
import re
import os


class Dishpatcher_email():
    """
    Class_Description:
    
         This class is dedicated to send the email to users
         based of the prediction i.e. recommendation of the courses.
         The message is send to all the user.

    
    Args:
        
        reciever_email :
                         type:<String>
                         Description: Email of the User

        subjects: 
                  type: <String>
                  Description: Subject of the mail

        message:
                type:<String>
                Description: Message bodyof the User
       
        Content_mail:
                type:<String> lowercase only
                Description: Mail body type plain or html
                Default value: plain


        Extracted from the .env file

        Email credentials: 
                

                smtp_server:
                            type: <String>
                Port:
                         type:<Int>
                         Descriptiosmtplib n: For TLS   
                account_host:
                             type: <String>
                app_password : 
                             type: <String>
        """
         
    def __init__(self,reciever_email,subject,message,Content_mail="plain"):
       
       
       
        """
        Constructor of the Dishpatcher_email used to
        initialise the variables

        """
 
       
        self.reciever_email= reciever_email
        self.subjects=subject
        self.message = message
        self.Content_mail =Content_mail
        
        #reading file from the .env file
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        File_Path = BASE_DIR +"/.env"
        
        env = environ.Env()
        environ.Env.read_env(File_Path)
        
        
        self.account_host = env('account_host')
        self.app_password = env('app_password')
        self.smtp_server = env('smtp_server')
        self.port = env('port')
    
       
        

    def send_email(self):

        """
        Description:
                Function: which sends email to the User.
               
      
        """
        
        msg = MIMEMultipart()
        msg['From'] = self.account_host
        msg['Subject'] = self.subjects
        msg['To'] = self.reciever_email

        if (self.Content_mail == "html"):
            msg.attach(MIMEText(self.message, 'html'))
        elif (self.Content_mail == "plain"):
            msg.attach(MIMEText(self.message, 'plain'))
        else:
            msg="Email-Dishpatcher-class >> Function - Send email : Mail content type is not correct !! try again with correct value" +" Contact_type : "+str(self.Content_mail)
            obj_logging = logging_information(msg)
            obj_logging.Logger_function_critical()
            #print(msg)    

        try:
          
            s = smtplib.SMTP(self.smtp_server , self.port) 
            
            
            try:
                
                s.starttls()
                s.login(msg['From'], self.app_password)
            
            
                try:
            
                    s.sendmail(msg['From'], msg['To'], msg.as_string()) 
                    s.quit() 
                    
                    
                    msg="Email-Dishpatcher-class >> Function - Send email : Mail sent successfully"+" Email :"+str(self.reciever_email)+ " Contact_type : "+str(self.Content_mail)
                    obj_logging = logging_information(msg)
                    obj_logging.Logger_function_critical()
                    #print(msg)
                

                except:
                    
                    msg="Email-Dishpatcher-class >> Function - Send email : Logged in but mail not Send"+" Reciever_Email :"+str(self.reciever_email)+ " Sender_Email:"+str(self.account_host)
                    obj_logging = logging_information(msg)
                    obj_logging.Logger_function_critical()
                    #print(msg)
                    
            except:
                
                
                msg="Email-Dishpatcher-class >> Function - Send email : Authentication failed"+" Email :"+str(self.account_host)
                obj_logging = logging_information(msg)
                obj_logging.Logger_function_critical()
                #print(msg)

        except: 
             
            msg="Email-Dishpatcher-class >> Function - Send email : Incorrect Smtp or Port"+ " Smtp :"+str(self.smtp_server)+" Port :"+str(self.port)
            obj_logging = logging_information(msg)
            obj_logging.Logger_function_critical()
            #print(msg)
             
          
        