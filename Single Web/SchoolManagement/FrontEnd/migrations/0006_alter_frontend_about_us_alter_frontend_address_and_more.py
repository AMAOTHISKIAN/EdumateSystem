# Generated by Django 4.1.6 on 2023-04-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0005_remove_frontend_about_cancution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontend',
            name='about_us',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='first_home_page_image',
            field=models.ImageField(upload_to='media/FrontEnd'),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='first_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='first_title_about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='owner_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='school_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='school_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='school_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='second_home_page_image',
            field=models.ImageField(upload_to='media/FrontEnd'),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='second_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='second_title_about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='third_home_page_image',
            field=models.ImageField(upload_to='media/FrontEnd'),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='third_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='third_title_about',
            field=models.TextField(),
        ),
    ]
