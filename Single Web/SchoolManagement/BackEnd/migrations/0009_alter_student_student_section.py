# Generated by Django 4.1.5 on 2023-01-05 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0008_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_Section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.section'),
        ),
    ]
