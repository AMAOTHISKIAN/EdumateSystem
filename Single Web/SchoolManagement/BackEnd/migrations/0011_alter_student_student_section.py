# Generated by Django 4.1.5 on 2023-01-05 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0010_alter_student_student_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_Section',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.section'),
        ),
    ]
