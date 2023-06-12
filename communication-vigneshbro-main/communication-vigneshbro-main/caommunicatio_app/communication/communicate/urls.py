

from .  import views 
from django.urls import include, path

from .views import (
                    smsfunction,
                    emailfunction,
                    watsappmsgfunction,
                    voicecall
                   )
urlpatterns = [


               path('message', views.message), 
               path('sms/',smsfunction.as_view(), name="Sms"),
               path('voicecall', voicecall.as_view(),name="call"), 
               path('email/',emailfunction.as_view(), name="Email"),
               path('watsappmsg/',watsappmsgfunction.as_view(), name="Watsappmsg"),
   
             ]
