# Generated by Django 2.0.2 on 2018-04-28 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180428_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='tên',
        ),
    ]