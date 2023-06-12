


import os
import re
import time
import environ
from .models import *
from faker import Faker
from twilio.rest import Client
from django.urls import reverse
from django.conf import settings
from .utility_functions import  *
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse,Gather






@csrf_exempt
def DataCorrection(request):

    if request.method == 'POST' or request.method == 'GET':

     

        if request.method == 'POST' :
           
            history_data, i             =           History.objects.get_or_create(
                                                                                    chatid = str(request.POST.get('CallSid')),
                                                                                 )


            history_data.called_from    =           str(request.POST.get('From')),
            history_data.called_caller  =           str(request.POST.get('Caller')),
            history_data.called_to      =           str(request.POST.get('From')),
            history_data.save()

        else:


            history_else, j             =           History.objects.get_or_create(
                                                                                    chatid = str(request.GET.get('CallSid')),
                                                                                 )
            history_else.called_from    =           str(request.GET.get('From')),
            history_else.called_caller  =           str(request.GET.get('Caller')),
            history_else.called_to      =           str(request.GET.get('From')),
            history_else.save()
        
        print("Inside personal_update view")
        path                            =           str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        read                            =           read_xml('DataCorrection',path)
        
        resp                            =           VoiceResponse()
        gather                          =           Gather(num_digits=1)
        resp.say(str(read),voice='Polly.Raveena', language='en-IN')
        resp.append(gather)


        if request.POST.get('Digits'):
       
            useraction_choice                   =                 {
                                                                      1:"Name Correction",
                                                                      2:"Email Correction",
                                                                      3:"Parent Name Correction",
                                                                      4:"Date of Birth Correction",
                                                                      5:"Mobile Number Correction",
                                                                     
                                                                  }
                                                                      



       
            choice                              =                   request.POST.get('Digits')

            user_action                         =                   " "

            if int(choice) in useraction_choice.keys():
                user_action                         =               user_action+str(choice)+ useraction_choice[int(choice)]

            else: 

                user_action                         =               user_action+str(choice)+ " Invalid Choice Entered"

            chatresponse_data                   =                   chatresponse.objects.create(
                                                                                                 human_request =user_action
                                                                                                )

            chatresponse_data.save()
            if request.method == 'GET':
                
                history, created        =           History.objects.get_or_create(
                                                                                    chatid    =   str(request.GET.get('CallSid')),
                                                                                 )  

                history.chat_history.add( chatresponse_data)
                history.save()

            if request.method == 'POST':
                
                history, created       =            History.objects.get_or_create(
                                                                                    chatid = str(request.POST.get('CallSid')),
                                                                                )   

                history.chat_history.add( chatresponse_data)
                history.save()
            
            
            if int(choice) == 1:
                print("Name Correction")
               

            elif int(choice) == 2:
                print("Email Correction")
                
                
            elif int(choice) == 3:
                 print("Parent Name Correction")

            elif int(choice) == 4:
                 print("Date of Birth Correction")

            elif int(choice) == 5:
                 print("Mobile Number Correction")

            
                
                

            elif int(choice) == 0:
                 print("Redirect maim")
                 return HttpResponseRedirect(reverse('home'))
                 
                                 
            else:

                print("Invalidinput")
                path                        =            str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                        =            read_xml('Invalidinput',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()
        
        else :
                        
                print("NoResponse")
                path                        =            str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                        =            read_xml('NoResponse',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()

        return HttpResponse(resp)

    else:

        return HttpResponse(str("No Call"))


@csrf_exempt
def LMSRelated(request):

    if request.method == 'POST' or request.method == 'GET':



        if request.method == 'POST' :
            

            history_data, i                 =            History.objects.get_or_create(
                                                                                       chatid = str(request.POST.get('CallSid')),
                                                                                      )
            history_data.called_from        =           str(request.POST.get('From')),
            history_data.called_caller      =           str(request.POST.get('Caller')),
            history_data.called_to          =           str(request.POST.get('From')),
            history_data.save()

        else:

        

            history_else, j                 =           History.objects.get_or_create(
                                                                                         chatid = str(request.GET.get('CallSid')),
                                                                                     )
            history_else.called_from        =           str(request.GET.get('From')),
            history_else.called_caller      =           str(request.GET.get('Caller')),
            history_else.called_to          =           str(request.GET.get('From')),
            history_else.save()
        
        print("Inside Linkdin and LMS Query")
        path                                =           str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        read                                =           read_xml('LMSRelated',path)
        
        resp                                =           VoiceResponse()
        gather                              =           Gather(num_digits=1)
        resp.say(str(read),voice='Polly.Raveena', language='en-IN')
        resp.append(gather)


        if request.POST.get('Digits'):
       
            useraction_choice                   =                 {
                                                                      1:"For Login Issue",
                                                                     
                                                                  }
                                                                      



       
            choice                              =                   request.POST.get('Digits')

            user_action                         =                   " "

            if int(choice) in useraction_choice.keys():
                user_action                         =               user_action+str(choice)+ useraction_choice[int(choice)]

            else: 

                user_action                         =               user_action+str(choice)+ " Invalid Choice Entered"

            chatresponse_data                   =                   chatresponse.objects.create(
                                                                                                 human_request =user_action
                                                                                                )

            chatresponse_data.save()
            if request.method == 'GET':
                history, created            =           History.objects.get_or_create(
                                                                                        chatid = str(request.GET.get('CallSid')),
                                                                                     )  

                history.chat_history.add( chatresponse_data)
                history.save()

            if request.method == 'POST':
                history, created           =            History.objects.get_or_create(
                                                                                        chatid = str(request.POST.get('CallSid')),
                                                                                    )   

                history.chat_history.add( chatresponse_data)
                history.save()
            
            
            if int(choice) == 1:
                print("Login Issue")
               
                
                
            elif int(choice) == 0:
                 print("Redirect maim")
                 return HttpResponseRedirect(reverse('home'))
                  
            else:

                

                print("Invalidinput")
                path                            =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                            =                   read_xml('Invalidinput',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()
        else :
                
                
                print("NoResponse")
                path                            =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                            =                   read_xml('NoResponse',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()

        return HttpResponse(resp)

    else:

        
        
        return HttpResponse(str("No Call"))


@csrf_exempt
def Programrelated(request):

    if request.method == 'POST' or request.method == 'GET':


        if request.method == 'POST' :

            history_data, i                 =                   History.objects.get_or_create(
                                                                                                chatid = str(request.POST.get('CallSid')),
                                                                                             )
            history_data.called_from        =                   str(request.POST.get('From')),
            history_data.called_caller      =                   str(request.POST.get('Caller')),
            history_data.called_to          =                   str(request.POST.get('From')),
            history_data.save()

        else:


            history_else, j                 =                   History.objects.get_or_create(
                                                                                                chatid = str(request.GET.get('CallSid'))
                                                                                             )
            history_else.called_from        =                   str(request.GET.get('From')),
            history_else.called_caller      =                   str(request.GET.get('Caller')),
            history_else.called_to          =                   str(request.GET.get('From')),
            history_else.save()
        
        print("Inside Change of Program, Batch and Elective ")
        path                                =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        read                                =                   read_xml('ProgramRelated',path)
        
        resp                                =                   VoiceResponse()
        gather                              =                   Gather(num_digits=1)
        resp.say(str(read),voice='Polly.Raveena', language='en-IN')
        resp.append(gather)


        if request.POST.get('Digits'):
       
            useraction_choice                   =                 {
                                                                      1:"Change of Elective",
                                                                      2:"Change of Program",
                                                                      3:"Change of Batch"
                                                                  }
                                                                      



       
            choice                              =                   request.POST.get('Digits')

            user_action                         =                   " "

            if int(choice) in useraction_choice.keys():
                user_action                         =               user_action+str(choice)+ useraction_choice[int(choice)]

            else: 

                user_action                         =               user_action+str(choice)+ " Invalid Choice Entered"

            chatresponse_data                   =                   chatresponse.objects.create(
                                                                                                 human_request =user_action
                                                                                                )

            chatresponse_data.save()
            if request.method == 'GET':
                history, created           =                    History.objects.get_or_create(
                                                                                                chatid = str(request.GET.get('CallSid'))
                                                                                             )  

                history.chat_history.add( chatresponse_data)
                history.save()

            if request.method == 'POST':

                history, created            =                   History.objects.get_or_create(
                                                                                                chatid = str(request.POST.get('CallSid'))
                                                                                              )   

                history.chat_history.add( chatresponse_data)
                history.save()
            
            
            if int(choice) == 1:
                print("Change of Elective")
               

            elif int(choice) == 2:
                print("Change of Program")

            elif int(choice) == 3:
                print("Change of Batch ")
                
                
            elif int(choice) == 0:
                 print("Redirect maim")
                 return HttpResponseRedirect(reverse('home'))
                  
            else:


                print("Invalidinput")
                path                       =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                       =                   read_xml('Invalidinput',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()
        else :
                
                
                print("NoResponse")
                path                        =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                        =                   read_xml('NoResponse',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()

        return HttpResponse(resp)

    else:
        
        return HttpResponse(str("No Call"))


@csrf_exempt
def collectnumber(request):

    if request.method == 'POST' or request.method == 'GET':

        

        if request.method == 'POST' :
           
            
            history_data, i                     =                   History.objects.get_or_create(
                                                                                                    chatid = str(request.POST.get('CallSid')),
                                                                                                 )
            history_data.called_from            =                   str(request.POST.get('From')),
            history_data.called_caller          =                   str(request.POST.get('Caller')),
            history_data.called_to              =                   str(request.POST.get('From')),
            history_data.save()


        if request.method == 'GET':
            
            history_else, j                     =                   History.objects.get_or_create(
                                                                                                    chatid = str(request.GET.get('CallSid')) 
                                                                                                 )
            history_else.called_from            =                   str(request.GET.get('From')),
            history_else.called_caller          =                   str(request.GET.get('Caller')),
            history_else.called_to              =                   str(request.GET.get('From')),
            history_else.save()



        path                                    =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        read                                    =                   read_xml('MainList',path)
        
        resp                                    =                   VoiceResponse()
        gather                                  =                   Gather(num_digits=10)
        resp.say(str("ENter ur number"),voice='Polly.Raveena', language='en-IN')
        resp.append(gather)
        
        if request.POST.get('Digits'):

            print(request.POST.get('Digits'))
            usernumber=str(request.POST.get('Digits'))
            length_usernumber=len(usernumber)
            print(length_usernumber)

            if length_usernumber ==10:
                print("ok")
                resp.say(str("ok"),voice='Polly.Raveena', language='en-IN')
            else:
                print("notok")
                resp.say(str("notok"),voice='Polly.Raveena', language='en-IN')


           
               
            




        return HttpResponse(resp)

    else:

        return HttpResponse(str("No Call"))


@csrf_exempt
def home(request):

    if request.method == 'POST' or request.method == 'GET':

        

        if request.method == 'POST' :
           
            
            history_data, i                     =                   History.objects.get_or_create(
                                                                                                    chatid = str(request.POST.get('CallSid')),
                                                                                                 )
            history_data.called_from            =                   str(request.POST.get('From')),
            history_data.called_caller          =                   str(request.POST.get('Caller')),
            history_data.called_to              =                   str(request.POST.get('From')),
            history_data.save()


        if request.method == 'GET':
            
            history_else, j                     =                   History.objects.get_or_create(
                                                                                                    chatid = str(request.GET.get('CallSid')) 
                                                                                                 )
            history_else.called_from            =                   str(request.GET.get('From')),
            history_else.called_caller          =                   str(request.GET.get('Caller')),
            history_else.called_to              =                   str(request.GET.get('From')),
            history_else.save()



        path                                    =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        read                                    =                   read_xml('MainList',path)
        
        resp                                    =                   VoiceResponse()
        gather                                  =                   Gather(num_digits=1)
        resp.say(str(read),voice='Polly.Raveena', language='en-IN')
        resp.append(gather)
        
        if request.POST.get('Digits'):

            useraction_choice                   =                 {
                                                                      1:"Fees Related",
                                                                      2:"Program Related",
                                                                      3:"Data Correction",
                                                                      4:"LMS Related",
                                                                      9:"Speak to Person"
                                                                  }



       
            choice                              =                   request.POST.get('Digits')

            user_action                         =                   " "

            if int(choice) in useraction_choice.keys():
                user_action                         =               user_action+str(choice)+ useraction_choice[int(choice)]

            else: 

                user_action                         =               user_action+str(choice)+ " Invalid Choice Entered"



            chatresponse_data                   =                   chatresponse.objects.create(
                                                                                                 human_request =user_action
                                                                                                )

            chatresponse_data.save()
            if request.method == 'GET':

                history, created                =                   History.objects.get_or_create(
                                                                                                    chatid = str(request.GET.get('CallSid'))
                                                                                                 )  

                history.chat_history.add( chatresponse_data)
                history.save()

            if request.method == 'POST':

                history, created                =                   History.objects.get_or_create(
                                                                                                    chatid = str(request.POST.get('CallSid'))
                                                                                                 )   

                history.chat_history.add( chatresponse_data)
                history.save()

            
            if int(choice) == 1:
                return HttpResponseRedirect(reverse('fees_related'))

            elif int(choice) == 2:
              
                return HttpResponseRedirect(reverse('prog_change'))
                
            elif int(choice) == 3:
                 return HttpResponseRedirect(reverse('personal_update'))

            elif int(choice) == 4:
                 return HttpResponseRedirect(reverse('LMS'))
            
            elif int(choice) == 9:
                 return HttpResponseRedirect(reverse('assistance'))

            elif int(choice) == 0:
                 return HttpResponseRedirect(reverse('home'))

            elif int(choice) == 5:
                print("Inside number")
                response = VoiceResponse()
                response.say("Enter ur number")
                
                return HttpResponseRedirect(('collectnumber'))

                 
                 
            else:
                
                print("Invalidinput")
                path                             =                      str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                             =                      read_xml('Invalidinput',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)

                resp.hangup()
        else :
                
                
                print("NoResponse")
                path                            =                       str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                            =                       read_xml('NoResponse',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()

        return HttpResponse(resp)

    else:

        return HttpResponse(str("No Call"))



@csrf_exempt
def feerelated(request):

    if request.method == 'POST' or request.method == 'GET':
        
        if request.method == 'POST' :
           
            history_data, i                      =                      History.objects.get_or_create(
                                                                                                            chatid = str(request.POST.get('CallSid'))
                                                                                                     )
            history_data.called_from             =                      str(request.POST.get('From')),
            history_data.called_caller           =                      str(request.POST.get('Caller')),
            history_data.called_to               =                      str(request.POST.get('From')),
            history_data.save()


        else:

            history_else, j                       =                     History.objects.get_or_create(
                                                                                                            chatid = str(request.GET.get('CallSid')),
                                                                                                     )
            history_else.called_from              =                     str(request.GET.get('From')),
            history_else.called_caller            =                     str(request.GET.get('Caller')),
            history_else.called_to                =                     str(request.GET.get('From')),
            history_else.save()

        print("Inside Fees Related ")
        
        path    =  str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        read = read_xml('feerelated',path)
        
        resp = VoiceResponse()
        gather = Gather(num_digits=1)
        resp.say(str(read),voice='Polly.Raveena', language='en-IN')
        resp.append(gather)


        if request.POST.get('Digits'):
       
            useraction_choice                   =                 {
                                                                      1:"Amount Mismatch",
                                                                      2:"Refund Request"
                                                                  }
                                                                      



       
            choice                              =                   request.POST.get('Digits')

            user_action                         =                   " "

            if int(choice) in useraction_choice.keys():
                user_action                         =               user_action+str(choice)+ useraction_choice[int(choice)]

            else: 

                user_action                         =               user_action+str(choice)+ " Invalid Choice Entered"

            chatresponse_data                   =                   chatresponse.objects.create(
                                                                                                 human_request =user_action
                                                                                                )

            chatresponse_data.save()

            if request.method == 'GET':

                history, created                =                       History.objects.get_or_create(
                                                                                                            chatid = str(request.GET.get('CallSid')),
                                                                                                      )  

                history.chat_history.add( chatresponse_data)
                history.save()

            if request.method == 'POST':

                history, created                =                       History.objects.get_or_create(
                                                                                                        chatid = str(request.POST.get('CallSid')),
                                                                                                     )   

                history.chat_history.add( chatresponse_data)
                history.save()
            
            
            if int(choice) == 1:
                print("Amount Mismatch ")
               

            elif int(choice) == 2:
                print("Refund Request")

          
                
            elif int(choice) == 0:
                 print("Redirect maim")
                 return HttpResponseRedirect(reverse('home'))
                  
            else:

                print("Invalidinput")
                path                            =                      str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                            =                      read_xml('Invalidinput',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()
        
        else :
                        
                print("NoResponse")
                path                            =                       str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                            =                       read_xml('NoResponse',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()

        return HttpResponse(resp)

    else:
        
        return HttpResponse(str("No Call"))



@csrf_exempt
def assistance(request):

    if request.method == 'POST' or request.method == 'GET':


        if request.method == 'POST' :
            
            history_data, i                     =                       History.objects.get_or_create(
                                                                                                        chatid = str(request.POST.get('CallSid'))
                                                                                                     )
            history_data.called_from            =                       str(request.POST.get('From')),
            history_data.called_caller          =                       str(request.POST.get('Caller')),
            history_data.called_to              =                       str(request.POST.get('From')),
            history_data.save()

            

        else:

        
            history_else, j                     =                       History.objects.get_or_create(
                                                                                                        chatid = str(request.GET.get('CallSid')),
                                                                                                     )
            history_else.called_from            =                       str(request.GET.get('From')),
            history_else.called_caller          =                       str(request.GET.get('Caller')),
            history_else.called_to              =                       str(request.GET.get('From')),
            history_else.save()
        
        print("Inside Speakperson")
        path                                    =                       str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
        read                                    =                       read_xml('Speakperson',path)
        
        resp                                    =                       VoiceResponse()
        gather                                  =                       Gather(num_digits=1)
        resp.say(str(read),voice='Polly.Raveena', language='en-IN')
        resp.append(gather)


        if request.POST.get('Digits'):
       
            useraction_choice                   =                 {
                                                                      1:"Recorded Instruction to use Josh",
                                                                      2:"Collect Info",
                                                                      3:"Connect to SPOC"
                                                                  }
                                                                      



       
            choice                              =                   request.POST.get('Digits')

            user_action                         =                   " "

            if int(choice) in useraction_choice.keys():
                user_action                         =               user_action+str(choice)+ useraction_choice[int(choice)]

            else: 

                user_action                         =               user_action+str(choice)+ " Invalid Choice Entered"

            chatresponse_data                   =                   chatresponse.objects.create(
                                                                                                 human_request =user_action
                                                                                                )

            chatresponse_data.save()
            if request.method == 'GET':
                history, created                =                       History.objects.get_or_create(
                                                                                                        chatid = str(request.GET.get('CallSid')),
                                                                                                     )  

                history.chat_history.add( chatresponse_data)
                history.save()

            if request.method == 'POST':
                history, created                =                       History.objects.get_or_create(
                                                                                                        chatid = str(request.POST.get('CallSid')),
                                                                                                     )   

                history.chat_history.add( chatresponse_data)
                history.save()
            
            
            if int(choice) == 1:
                print("For Recorded Instruction to use Josh")
               

            elif int(choice) == 2:
                print("Collect Info")
                
                
            elif int(choice) == 3:
                 print("Connect to SPOC")

            
                            

            elif int(choice) == 0:
                 print("Redirect maim")
                 return HttpResponseRedirect(reverse('home'))
                 
                                 
            else:

                print("Invalidinput")
                path                           =                    str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                           =                    read_xml('Invalidinput',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()
        
        else :
                        
                print("NoResponse")
                path                            =                   str(settings.BASE_DIR)+"/call/Call_saved_xml/IVR.xml"
                read                            =                   read_xml('NoResponse',path)
                resp.say(str(read),voice='Polly.Raveena', language='en-IN')
                resp.append(gather)
                resp.hangup()

        return HttpResponse(resp)

    else:

        return HttpResponse(str("No Call"))

