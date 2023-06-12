from django.db import models
from django.utils import timezone

class chatresponse(models.Model):

    human_request   = models.CharField(max_length=100,null=True, blank=True)
    created_at      = models.DateTimeField(default=timezone.now ,null=True, blank=True)

    
   
class History(models.Model):

    chatid          = models.CharField(max_length=100, null=True, blank=True)
    called_from     = models.CharField(max_length=100, null=True, blank=True)
    called_caller   = models.CharField(max_length=100, null=True, blank=True)
    called_to       = models.CharField(max_length=100, null=True, blank=True)
    chat_history    = models.ManyToManyField(chatresponse, null=True, blank=True)
    created_at      = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.chatid

