from django import forms
from django.forms.models import ModelForm

from Reading.models import ReadingBook

from django.contrib.auth.models import User

from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateNewReadingBook(forms.ModelForm):
    class Meta : 
        model = ReadingBook
        fields = (
            'name',
            'content_reading',    
        )

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"

