# Generated by Django 2.0.2 on 2019-06-28 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
