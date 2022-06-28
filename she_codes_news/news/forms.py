from django import forms
from django.forms import ModelForm

from users.models import CustomUser
from .models import NewsStory, Category
from users.models import CustomUser

# choices = Category.objects.all().values_list('name', 'name')

choices_list = []

# for item in choices:
#     choices_list.append(item)

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'category', 'content', 'image']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs=
            {'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            }
        writer = CustomUser.username
        
    def AccessWriterName(self):
        writer = CustomUser.username
        return writer


class StoryFormUpdate(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'content', 'image', 'category',]
