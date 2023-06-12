

 
from .  import views 
from django.urls import include, path
#

urlpatterns = [


              path('home/', views.home,name='home'),
              path('collectnumber/', views.collectnumber,name='collectnumber'), 
              path('LMS_update/', views.LMSRelated,name='LMS'),
              path('assistance/', views.assistance,name='assistance'),
              path('fees_related/', views.feerelated,name='fees_related'),
              path('change_prog/', views.Programrelated,name='prog_change'),
              path('Personal_update/', views.DataCorrection,name='personal_update'),
   

             ]
