# Generated by Django 3.2.7 on 2021-10-22 02:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_expense_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income', to='budget.project')),
            ],
            options={
                'ordering': ('-amount',),
            },
        ),
    ]
