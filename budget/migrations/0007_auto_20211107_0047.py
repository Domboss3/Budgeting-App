# Generated by Django 3.2.7 on 2021-11-07 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0006_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.CharField(default='housing', max_length=255),
        ),
    ]
