# Generated by Django 4.1.6 on 2023-02-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0047_class_annual_fee_class_exams_fee_class_monthly_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_type', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.IntegerField(default=2)),
                ('year', models.IntegerField(default=2023)),
                ('payment_method', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.student')),
            ],
        ),
    ]
