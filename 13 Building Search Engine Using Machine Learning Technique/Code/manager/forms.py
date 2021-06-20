from django import forms
from manager.models import *
from django.core import validators

class managerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(),required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        model=managerModel
        fields=['name','passwd','cwpasswd','email','mobileno','status']



class UploadfileForm(forms.ModelForm):

    class Meta:
        model = uploadmodel
        fields = ('filename','filetype','file')



