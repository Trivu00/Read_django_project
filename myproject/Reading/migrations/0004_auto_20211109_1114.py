# Generated by Django 3.2.8 on 2021-11-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reading', '0003_readingbook_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readingbook',
            name='item_image',
        ),
        migrations.AddField(
            model_name='readingbook',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
