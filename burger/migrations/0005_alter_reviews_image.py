# Generated by Django 4.1.2 on 2022-11-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0004_alter_reviews_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='image',
            field=models.FileField(blank=True, upload_to='reviews/'),
        ),
    ]
