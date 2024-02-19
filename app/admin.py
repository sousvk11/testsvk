from django.contrib import admin
from app.models import usr_reg


# Register your models here.
class user_details(admin.ModelAdmin):
   list_display=('name','email','passwd')

admin.site.register(usr_reg,user_details)      