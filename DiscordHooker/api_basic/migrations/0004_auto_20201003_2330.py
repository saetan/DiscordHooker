# Generated by Django 3.1.1 on 2020-10-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_auto_20201003_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]