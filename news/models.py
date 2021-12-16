from django.db import models
from django.db.models.fields import CharField


class Articles(models.Model):

    title = models.CharField('Назавание', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text  = models.TextField('Статья')
    date  = models.DateTimeField('Дата публикации')

    def  __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость' 
        verbose_name_plural = 'Новости' 


