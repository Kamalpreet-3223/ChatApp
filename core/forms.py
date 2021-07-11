from django import forms
from django.forms import fields, widgets
from .models import Messages


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message', ]
        widgets = {
            'message': forms.TextInput(attrs={'class': 'msgbox'})
        }
