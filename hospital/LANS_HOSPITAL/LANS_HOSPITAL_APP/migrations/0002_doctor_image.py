# Generated by Django 5.1 on 2024-09-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LANS_HOSPITAL_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
