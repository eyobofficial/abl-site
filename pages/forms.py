from django import forms
from . import models


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = ('email', )


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ('name', 'email', 'subject', 'content', )
