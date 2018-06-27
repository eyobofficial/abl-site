from django import forms
from . import models


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = ('email', )