# Generated by Django 3.0.5 on 2020-10-30 02:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0005_auto_20201028_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorrequest',
            name='desired_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]