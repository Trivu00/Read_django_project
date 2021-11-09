# Generated by Django 3.2.8 on 2021-11-08 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Reading', '0002_alter_readingbook_read_write'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingbook',
            name='item_image',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
