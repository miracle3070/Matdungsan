# Generated by Django 3.1 on 2020-09-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='completeMT',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]