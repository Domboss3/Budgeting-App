# Generated by Django 3.2.7 on 2021-10-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20211020_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Bills & Utilities', 'Bills & Utilities')], max_length=100),
        ),
    ]