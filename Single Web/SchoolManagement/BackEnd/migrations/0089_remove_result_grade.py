# Generated by Django 4.1.6 on 2023-04-08 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0088_remove_result_total_marks_remove_subject_pactical'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='grade',
        ),
    ]
