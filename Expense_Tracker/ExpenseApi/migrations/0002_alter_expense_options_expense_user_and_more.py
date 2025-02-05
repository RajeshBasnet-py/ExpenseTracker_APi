# Generated by Django 5.1.4 on 2025-01-08 15:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date'], 'verbose_name': 'Expense', 'verbose_name_plural': 'Expenses'},
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Groceries', 'Groceries'), ('Leisure', 'Leisure'), ('Electronics', 'Electronics'), ('Utilities', 'Utilities'), ('Clothing', 'Clothing'), ('Health', 'Health'), ('Others', 'Others')], max_length=100),
        ),
    ]
