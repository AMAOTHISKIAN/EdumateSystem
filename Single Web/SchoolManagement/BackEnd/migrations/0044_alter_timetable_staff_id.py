# Generated by Django 4.1.6 on 2023-02-15 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0043_timetable_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.staff'),
        ),
    ]
