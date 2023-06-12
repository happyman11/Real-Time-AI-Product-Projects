

from django.contrib import admin
from .models import (
                        Sms_detail, 
                        Email_detail, 
                        Watsapp_detail,
                        call_detail
                    )
                


admin.site.register(Sms_detail)
admin.site.register(call_detail)
admin.site.register(Email_detail)
admin.site.register(Watsapp_detail)