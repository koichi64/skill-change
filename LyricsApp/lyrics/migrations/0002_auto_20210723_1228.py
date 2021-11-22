# Generated by Django 3.2.5 on 2021-07-23 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lyrics', to='lyrics.song', verbose_name='曲'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='lyrics.artist', verbose_name='アーティスト'),
        ),
    ]
