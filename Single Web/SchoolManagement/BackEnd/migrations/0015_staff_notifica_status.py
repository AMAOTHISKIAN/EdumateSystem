# Generated by Django 4.1.5 on 2023-01-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0014_staff_notifica'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notifica',
            name='status',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
