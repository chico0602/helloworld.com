# Generated by Django 2.2.9 on 2020-02-16 06:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='動画タイトル')),
                ('thumbnail', models.ImageField(blank=True, upload_to='', verbose_name='動画サムネイル')),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'mpeg', 'mpg', 'avi', 'wmv', 'flv', ''])], verbose_name='動画ファイル')),
            ],
        ),
    ]
