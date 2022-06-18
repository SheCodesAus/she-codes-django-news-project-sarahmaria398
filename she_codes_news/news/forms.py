from django import forms
from django.forms import ModelForm
from .models import NewsStory
from users.models import CustomUser

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image']
        widgets = {'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs=
        {'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}




class StoryFormUpdate(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'content', 'image']
