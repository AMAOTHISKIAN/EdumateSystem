# Generated by Django 4.1.5 on 2023-01-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=70)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_Name', models.CharField(max_length=100)),
                ('Owner_Name', models.CharField(max_length=100)),
                ('School_email', models.CharField(max_length=100)),
                ('School_Number', models.CharField(max_length=100)),
                ('Frist_title', models.CharField(max_length=100)),
                ('Frist_title_about', models.TextField()),
                ('Second_title', models.CharField(max_length=100)),
                ('Second_title_about', models.TextField()),
                ('Thried_title', models.CharField(max_length=100)),
                ('Thried_title_about', models.TextField()),
                ('About_us', models.TextField()),
                ('About_Points', models.TextField()),
                ('About_Cancution', models.TextField()),
                ('Perents_Image_3', models.ImageField(upload_to='media/FrontEnd')),
                ('Perents_Image_3_bio', models.TextField()),
                ('Perents_Image_2', models.ImageField(upload_to='media/FrontEnd')),
                ('Perents_Image_2_bio', models.TextField()),
                ('Perents_Image_1', models.ImageField(upload_to='media/FrontEnd')),
                ('Perents_Image_1_bio', models.TextField()),
                ('Teacher_Image_1', models.ImageField(upload_to='media/FrontEnd')),
                ('Teacher_Image_1_bio', models.TextField()),
                ('Teacher_Image_2', models.ImageField(upload_to='media/FrontEnd')),
                ('Teacher_Image_2_bio', models.TextField()),
                ('Teacher_Image_3', models.ImageField(upload_to='media/FrontEnd')),
                ('Teacher_Image_3_bio', models.TextField()),
                ('Teacher_Image_4', models.ImageField(upload_to='media/FrontEnd')),
                ('Teacher_Image_4_bio', models.TextField()),
                ('About_page', models.ImageField(upload_to='media/FrontEnd')),
                ('Home_page', models.ImageField(upload_to='media/FrontEnd')),
                ('School_video', models.FileField(upload_to='media/FrontEnd')),
                ('Address', models.TextField()),
            ],
        ),
    ]
