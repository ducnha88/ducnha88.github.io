# Generated by Django 2.0.2 on 2018-04-28 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='tittle',
            new_name='title',
        ),
    ]
