


from .models import Sms_detail,Email_detail,Watsapp_detail,call_detail
from rest_framework import serializers


class sms_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Sms_detail
        fields = ['Countrycode','Number','Content']



class Email_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Email_detail
        fields = ['reciepient','subject','Content']



class watsapp_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Watsapp_detail
        fields = ['Countrycode','Number','Content']


class call_Serializer(serializers.ModelSerializer):


    class Meta:
        model = call_detail
        fields = ['Countrycode','Number','Content']