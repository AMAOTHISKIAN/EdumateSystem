# Generated by Django 4.1.6 on 2023-03-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0064_stop_vehicles_route_bus_rider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'STAFFS'), (3, 'GUEST'), (4, 'TeacherT')], default=1, max_length=58),
        ),
    ]
