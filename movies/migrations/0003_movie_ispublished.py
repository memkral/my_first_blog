# Generated by Django 3.0.3 on 2020-06-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200622_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
    ]
