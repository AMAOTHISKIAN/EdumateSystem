# Generated by Django 4.1.5 on 2023-01-04 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frontend',
            old_name='Home_page',
            new_name='Frist_Home_page_image',
        ),
        migrations.RenameField(
            model_name='frontend',
            old_name='Perents_Image_1',
            new_name='Second_home_page_image',
        ),
        migrations.RenameField(
            model_name='frontend',
            old_name='Perents_Image_2',
            new_name='Third_Home_page_image',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Perents_Image_1_bio',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Perents_Image_2_bio',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Perents_Image_3',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Perents_Image_3_bio',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_1',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_1_bio',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_2',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_2_bio',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_3',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_3_bio',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_4',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='Teacher_Image_4_bio',
        ),
    ]
