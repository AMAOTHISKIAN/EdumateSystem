# Generated by Django 4.1.5 on 2023-01-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0017_student_leave_guest_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_notifica',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
