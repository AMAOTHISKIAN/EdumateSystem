# Generated by Django 4.1.6 on 2023-04-09 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0004_category_image'),
        ('Blogs', '0002_alter_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='section',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.category'),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
