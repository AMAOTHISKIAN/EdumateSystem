# Generated by Django 4.1.6 on 2023-04-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0013_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
