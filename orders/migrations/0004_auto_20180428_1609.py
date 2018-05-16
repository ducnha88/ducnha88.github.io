# Generated by Django 2.0.2 on 2018-04-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180428_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='post_code',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='số điện thoại'),
        ),
    ]
