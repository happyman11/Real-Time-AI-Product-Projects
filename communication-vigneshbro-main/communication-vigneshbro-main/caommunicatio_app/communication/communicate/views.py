

from .serializers import (
                                sms_Serializer,
                                Email_Serializer,
                                watsapp_Serializer,
                                call_Serializer
                         )

from .models import (
                        Sms_detail,
                        Email_detail,
                        Watsapp_detail,
                        call_detail
                    )

import os
import re
import environ
from twilio.rest import Client
from faker import Faker
from os.path import join
from os.path import exists
from os.path import dirname
from django.conf import settings
from .chatbot_utilities import *
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from  .sms_function import Dishpatcher_sms
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail,EmailMultiAlternatives
from twilio.twiml.messaging_response import MessagingResponse
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication



class smsfunction(APIView):


    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    serializer_class=sms_Serializer

    def post(self, request, format=None):

        Country_code =  request.data.get('Countrycode')
        phone_number =  request.data.get('Number')
        content      =  request.data.get('Content')

        if phone_number and content and Country_code:

            if len(str(phone_number)) == 10:


                reciever_number=str(Country_code)+str(phone_number)

                sms_class=Dishpatcher_sms()
                send_sms=sms_class.send_sms_twillio( content,reciever_number)

                sms_data=Sms_detail(
                                        Countrycode  =Country_code,
                                        Number       =reciever_number,
                                        Content      =content,
                                        msgid        =send_sms["sms.sid"],
                                        status       =send_sms["response"]
                                   )

                sms_data.save()


                return Response(send_sms)

            else:

                if len(str(phone_number)) >10:

                    reciever_number=str(Country_code)+str(phone_number)
                    sms_data=Sms_detail(
                                             Countrycode  =Country_code,
                                             Number       =phone_number,
                                             Content      =content,
                                             msgid        ="None",
                                             status       ="Please check the input Number (more than 10)"
                                       )

                    sms_data.save()

                    dev                  = {}
                    dev["response"]      = "Please check the input Number (more than 10)"
                    dev["Provided By:"]  = "Chadura Communication Api Services"
                    dev["status"]        =  400

                    return Response(dev)

                else:

                    reciever_number=str(Country_code )+str(phone_number)
                    sms_data=Sms_detail(
                                          Countrycode  =Country_code,
                                          Number       =phone_number,
                                          Content      =content,
                                          msgid        ="None",
                                          status       ="Please check the input Number (less than 10)"

                                       )

                    sms_data.save()

                    dev                   = {}
                    dev["response"]       = "Please check the input Number (less than 10)"
                    dev["Provided By:"]   = "Chadura Communication Api Services"
                    dev["status"]         =  400

                    return Response(dev)




        else:

                reciever_number=str(Country_code )+str(phone_number)
                sms_data=Sms_detail(
                                         Countrycode  =Country_code,
                                         Number       =phone_number,
                                         Content      =content,
                                         msgid        ="None",
                                         status       ="Input Arguments is empty"

                                   )

                sms_data.save()


                dev                     = {}
                dev["response"]         = "Input Arguments is empty"
                dev["Provided By:"]     = "Chadura Communication Api Services"
                dev["status"]           = 400

                return Response(dev)




class emailfunction(APIView):



    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    serializer_class=Email_Serializer

    def post(self, request, format=None):


        reciepient  =  request.data.get('reciepient')
        subject     =  request.data.get('subject')
        Content     =  request.data.get('Content')

        if reciepient and subject and Content :

            email_Searched = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(reciepient), flags=0)

            if email_Searched:



                try:

                    msg                 = EmailMultiAlternatives(subject,Content, settings.EMAIL_HOST_USER, [reciepient])
                    msg.content_subtype = "html"
                    msg.send()

                    Email_data =Email_detail(
                                                reciepient  = reciepient,
                                                subject     = subject,
                                                Content     = Content,
                                                status      = "Mail Sent Successfully"
                                            )



                    Email_data.save()


                    dev                  = {}
                    dev["response"]      = "Mail Sent Successfully"
                    dev["Provided By:"]  = "Chadura Communication Api Services"
                    dev["status"]        =  200

                    return Response(dev)


                except:

                    Email_data =Email_detail(
                                                reciepient  = reciepient,
                                                subject     = subject,
                                                Content     = Content,
                                                status      = "Mail Sending Failed"
                                            )



                    Email_data.save()


                    dev                  =   {}
                    dev["response"]      =   "Mail Sending Failed"
                    dev["Provided By:"]  =   "Chadura Communication Api Services"
                    dev["status"]        =   400

                    return Response(dev)


            else:


                Email_data =Email_detail (

                                            reciepient  =  reciepient,
                                            subject     =  subject,
                                            Content     =  Content,
                                            status      =  "Email is missing in recipient email"

                                         )

                Email_data.save()



                dev                  =   {}
                dev["response"]      =  "Email is missing in recipient email"
                dev["Provided By:"]  =  "Chadura Communication Api Services"
                dev["status"]        =   400

                return Response(dev)



        else:


            Email_data =Email_detail(

                                      reciepient  =  reciepient,
                                      subject     =  subject,
                                      Content     =  Content,
                                      status      =  "Input Arguments is empty"

                                    )

            Email_data.save()

            dev                  =   {}
            dev["response"]      =   "Input Arguments is empty"
            dev["Provided By:"]  =   "Chadura Communication Api Services"
            dev["status"]        =   400

            return Response(dev)


class watsappmsgfunction(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    serializer_class=watsapp_Serializer



    def post(self, request, format=None):

        Country_code =  request.data.get('Countrycode')
        phone_number =  request.data.get('Number')
        content      =  request.data.get('Content')

        if phone_number and content and Country_code:

            if len(str(phone_number)) == 10:


                reciever_number=str(Country_code)+str(phone_number)

                sms_class=Dishpatcher_sms()
                send_sms=sms_class.send_watsappsms_twillio( content,reciever_number)

                sms_data=Watsapp_detail(
                                        Countrycode  =Country_code,
                                        Number       =phone_number,
                                        Content      =content,
                                        msgid        =send_sms["sms.sid"],
                                        status       =send_sms["response"]
                                      )

                sms_data.save()


                return Response(send_sms)

            else:

                if len(str(phone_number)) >10:

                    reciever_number=str(Country_code)+str(phone_number)
                    sms_data=Watsapp_detail(
                                             Countrycode  =Country_code,
                                             Number       =phone_number,
                                             Content      =content,
                                             msgid        ="None",
                                             status       ="Please check the input Number (more than 10)"
                                           )

                    sms_data.save()

                    dev                  = {}
                    dev["response"]      = "Please check the input Number (more than 10)"
                    dev["Provided By:"]  = "Chadura Communication Api Services"
                    dev["status"]        =  400

                    return Response(dev)

                else:

                    reciever_number=str(Country_code)+str(phone_number)
                    sms_data=Watsapp_detail(

                                            Countrycode  =Country_code,
                                            Number       =phone_number,
                                            Content      =content,
                                            msgid        ="None",
                                            status       ="Please check the input Number (less than 10)"

                                           )

                    sms_data.save()

                    dev                   = {}
                    dev["response"]       = "Please check the input Number (less than 10)"
                    dev["Provided By:"]   = "Chadura Communication Api Services"
                    dev["status"]         =  400

                    return Response(dev)




        else:

                reciever_number=str(Country_code )+str(phone_number)
                sms_data=Watsapp_detail(

                                         Countrycode  =Country_code,
                                         Number       =phone_number,
                                         Content      =content,
                                         msgid        ="None",
                                         status       ="Input Arguments is empty"

                                       )

                sms_data.save()


                dev                     = {}
                dev["response"]         = "Input Arguments is empty"
                dev["Provided By:"]     = "Chadura Communication Api Services"
                dev["status"]           = 400

                return Response(dev)







@csrf_exempt
def message(request):

    if request.method == 'POST':

        user = request.POST.get('From')
        message = request.POST.get('Body')
        print(f'{user} says {message}')
        fake = Faker()

        name=fake.name()
        response1=send(str(message),str(name),request)
        print("response:::",response1)




        resp = MessagingResponse()


        reply=resp.message()

        response_touser=str(response1["text"])



        keys_list=list(response1.keys())

        print(keys_list)



        #urls
        if "urls" in keys_list :
            for i in response1["urls"]:
                keys_urls=list(i.keys())
                for j in keys_urls:

                    response_touser=response_touser+ " "+str(i[j])
                    print(i[j])

        reply.body(response_touser)








        return HttpResponse(str(resp))

    else:


        response = MessagingResponse()
        response.message('No message Recieved')
        return HttpResponse(str(response))







class voicecall(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    serializer_class=call_Serializer



    def post(self, request, format=None):

        Country_code =  request.data.get('Countrycode')
        phone_number =  request.data.get('Number')
        content      =  request.data.get('Content')

        if phone_number and content and Country_code:

            if len(str(phone_number)) == 10:


                reciever_number=str(Country_code)+str(phone_number)

                sms_class=Dishpatcher_sms()
                send_sms=sms_class.call_twilio( content,reciever_number)

                sms_data=call_detail(
                                         Countrycode  =Country_code,
                                         Number       =phone_number,
                                         Content      =content,
                                         msgid        =send_sms["call.sid"],
                                         status       =send_sms["response"]
                                       )

                sms_data.save()


                return Response(send_sms)

            else:

                if len(str(phone_number)) >10:

                    reciever_number=str(Country_code)+str(phone_number)
                    sms_data=call_detail(
                                             Countrycode  =Country_code,
                                             Number       =phone_number,
                                             Content      =content,
                                             msgid        ="None",
                                             status       ="Please check the input Number (more than 10)"
                                        )

                    sms_data.save()

                    dev                  = {}
                    dev["response"]      = "Please check the input Number (more than 10)"
                    dev["Provided By:"]  = "Chadura Communication Api Services"
                    dev["status"]        =  400

                    return Response(dev)

                else:

                    reciever_number=str(Country_code)+str(phone_number)
                    sms_data=call_detail(

                                            Countrycode  =Country_code,
                                            Number       =phone_number,
                                            Content      =content,
                                            msgid        ="None",
                                            status       ="Please check the input Number (less than 10)"

                                           )

                    sms_data.save()

                    dev                   = {}
                    dev["response"]       = "Please check the input Number (less than 10)"
                    dev["Provided By:"]   = "Chadura Communication Api Services"
                    dev["status"]         =  400

                    return Response(dev)




        else:

                reciever_number=str(Country_code )+str(phone_number)
                sms_data=call_detail(

                                         Countrycode  =Country_code,
                                         Number       =phone_number,
                                         Content      =content,
                                         msgid        ="None",
                                         status       ="Input Arguments is empty"

                                       )

                sms_data.save()


                dev                     = {}
                dev["response"]         = "Input Arguments is empty"
                dev["Provided By:"]     = "Chadura Communication Api Services"
                dev["status"]           = 400

                return Response(dev)

    