# Generated by Django 4.1.6 on 2023-03-07 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0057_remove_hostel_capacity_room_room_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
        ),
    ]
