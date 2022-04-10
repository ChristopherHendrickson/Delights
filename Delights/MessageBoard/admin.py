from django.contrib import admin

# Register your models here.
from .models import *

class MessageAppAdmin(admin.ModelAdmin):
    list_display = ("message",)


admin.site.register(Message, MessageAppAdmin)