# Generated by Django 5.0.1 on 2024-02-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customuser_credentials_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
