from django.db import models
from django.db.models import fields
# from news.models import Articles
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
    
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации. Пример: 2011-12-13 14:15:16',
            }),

            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),

        }

