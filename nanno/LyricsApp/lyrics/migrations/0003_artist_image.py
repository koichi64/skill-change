# Generated by Django 3.2.5 on 2021-07-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0002_auto_20210723_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像'),
        ),
    ]
