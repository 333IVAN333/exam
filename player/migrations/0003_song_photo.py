# Generated by Django 4.0.2 on 2022-02-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_alter_timecode_text_alter_timecode_transcription'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/', verbose_name='Обложка песни'),
        ),
    ]
