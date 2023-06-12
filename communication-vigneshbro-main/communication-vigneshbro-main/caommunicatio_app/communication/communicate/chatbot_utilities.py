import os
import re
import json
import django
import random
import environ
import requests
from os.path import join
from os.path import exists
from os.path import dirname
from textblob import TextBlob
from better_profanity import profanity












def call_api(message,session_id):

    headersList             =   {
                                        "Accept": "*/*",
                                        "Content-Type": "application/json",
                                        "User-Agent": 'Thunder Client (https://www.thunderclient.com)',
                                        "Authorization":'Token c7f8fde48776fc563962460ab7b204f8f2f4c2c9',
                                }
    
    user_input              =   str(message)
    
  
  
    reqUrl                  =   'http://localhost:5005/webhooks/rest/webhook'
    payload                 =   json.dumps({"sender":session_id,"message":user_input})

    response                =   requests.request("POST", reqUrl, data=payload,  headers=headersList)
    

    chatbot_reply           =   response.json()





    if (len(chatbot_reply)>0):

        keys_response       =   list(chatbot_reply[0].keys())
       




        if ("custom" not in keys_response):
            response_json={}
            
            for i in keys_response:
                link        =   []
                buttons     =   []
                if i == "buttons":
               

                    for j in chatbot_reply[0][i]:
               
                        keys_exist      =       list(j.keys())


                        if ('link' in keys_exist):
                   
                            link.append(j)
                        else:
                            
                            buttons.append(j)

               
                    response_json["urls"]               =               link
                    response_json["buttons"]            =               buttons


                else:

                    response_json[str(i)]               =               chatbot_reply[0][i]
            response_json["save"]       =               1
                
            return(response_json)

        elif ('custom' in keys_response):
            response_json       =       {}
            response_json["recipient_id"]       =       chatbot_reply[0]["recipient_id"]

            custom_keys     =       keys_custom=chatbot_reply[0]["custom"].keys()
           
            for i in custom_keys:
                response_json[str(i)]       =       chatbot_reply[0]["custom"][i]
            response_json["save"]       =       1
            return(response_json)

        else:

            response_dict       =       {}
            response_dict["recipient_id"]       =       "user"
            response_dict["text"]       =       "No reply for chatbot"
            response_dict["buttons"]        =       None
            response_dict["urls"]           =None
            response_json["save"]=1
            return(response_dict)



def send(msg,session_id,request):


    text = TextBlob(msg)
    # textCorrected = text.correct()
    # print("textCorrected::",textCorrected)

    


     
   
    res=call_api(str(msg),session_id)
        # print("Res output:::",res)
        
        
    keys_custom= list(res.keys())
    print("For Connect to agent",keys_custom)
    return(res)
