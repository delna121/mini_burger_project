# Generated by Django 4.1.2 on 2022-11-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='image',
            field=models.ImageField(default=True, upload_to='reviews'),
        ),
    ]