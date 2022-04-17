
from cProfile import label
import imp
from pyexpat import model
from django import forms
from .models import Student

class SimpleForm(forms.Form):
    name= forms.CharField()
    lastname=forms.CharField()


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email']
        labels={"name":"Enter Name", 'email':'Enter Email'}
        help_text={"name":"enter your name"}
