# Generated by Django 4.1.5 on 2023-01-26 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0025_rename_student_attendancerecord_student_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AttendanceRecord',
        ),
    ]
