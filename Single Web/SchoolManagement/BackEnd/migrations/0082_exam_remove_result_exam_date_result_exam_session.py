# Generated by Django 4.1.6 on 2023-04-01 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0081_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(choices=[('firstterm', 'First Exam'), ('midterm', 'Midterm Exam'), ('final', 'Final Exam'), ('quiz', 'Quiz')], max_length=255)),
                ('session_year', models.IntegerField()),
                ('session_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam_date',
        ),
        migrations.AddField(
            model_name='result',
            name='exam_Session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BackEnd.exam'),
        ),
    ]
