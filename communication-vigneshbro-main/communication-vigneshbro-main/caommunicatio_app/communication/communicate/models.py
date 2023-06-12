

from django.db import models
from django.utils import timezone



class Sms_detail(models.Model):


  Countrycode  =  models.CharField(max_length=6,default=+91)
  Number       =  models.CharField(max_length=10)
  Content      =  models.CharField(max_length=200)
  msgid        =  models.CharField(max_length=30)
  status       =  models.CharField(max_length=100)
  sent_at      =  models.DateTimeField(default=timezone.now ,null=True, blank=True)

  def __str__(self):
        
      return " Sent Time::  {} || Status:: {}  ||  Message ID:: {}".format( self.sent_at, self.status, self.msgid)

  def save(self, *args, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        return super(Sms_detail, self).save(*args, **kwargs)



class Email_detail(models.Model):

  reciepient   = models.EmailField()
  subject      = models.CharField(max_length=200)
  Content      = models.TextField()
  status       = models.CharField(max_length=100)
  sent_at      = models.DateTimeField(default=timezone.now ,null=True, blank=True)

  def __str__(self):
        
      return " Sent Time::  {} || Reciepient:: {}  ||  Status:: {}".format( self.sent_at, self.reciepient , self.status )
  def save(self, *args, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        return super(Email_detail, self).save(*args, **kwargs)



class Watsapp_detail(models.Model):

  Countrycode  =  models.CharField(max_length=6,default=+91)
  Number       = models.CharField(max_length=10)
  Content      = models.CharField(max_length=200)
  msgid        = models.CharField(max_length=30)
  status       = models.CharField(max_length=100)
  sent_at      = models.DateTimeField(default=timezone.now ,null=True, blank=True)

  def __str__(self):
        
      return " Sent Time::  {} || Status:: {}  ||  Message ID:: {}".format( self.sent_at, self.status, self.msgid)

  def save(self, *args, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        return super( Watsapp_detail, self).save(*args, **kwargs)

class call_detail(models.Model):

  Countrycode  =  models.CharField(max_length=6,default=+91)
  Number       = models.CharField(max_length=10)
  Content      = models.CharField(max_length=200)
  msgid        = models.CharField(max_length=30)
  status       = models.CharField(max_length=100)
  sent_at      = models.DateTimeField(default=timezone.now ,null=True, blank=True)

  def __str__(self):
        
      return " Sent Time::  {} || Status:: {}  ||  Message ID:: {}".format( self.sent_at, self.status, self.msgid)

  def save(self, *args, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        return super(call_detail, self).save(*args, **kwargs)