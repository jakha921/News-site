# Generated by Django 3.2.2 on 2021-08-01 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aeticles',
            new_name='Articles',
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]