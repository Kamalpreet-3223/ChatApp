from django.contrib import admin
from .models import Messages

# Register your models here.


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message', ]
