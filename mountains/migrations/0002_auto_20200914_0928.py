# Generated by Django 3.1.1 on 2020-09-14 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mountains', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completedmt',
            old_name='mountain',
            new_name='mountain_id',
        ),
        migrations.RenameField(
            model_name='completedmt',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='completedmt',
            name='mountain_id',
            field=models.ForeignKey(db_column='mountain_id', on_delete=django.db.models.deletion.CASCADE, to='mountains.mountain'),
        ),
        migrations.AlterField(
            model_name='completedmt',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
