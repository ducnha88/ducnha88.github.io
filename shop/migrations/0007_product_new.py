# Generated by Django 2.0.2 on 2018-05-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180510_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
