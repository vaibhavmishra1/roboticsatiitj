# Generated by Django 2.0.2 on 2019-07-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_issuematerial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuematerial',
            old_name='description',
            new_name='item',
        ),
        migrations.AddField(
            model_name='issuematerial',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
