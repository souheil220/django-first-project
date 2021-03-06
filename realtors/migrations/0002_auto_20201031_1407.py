# Generated by Django 3.1.2 on 2020-10-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='photos',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
