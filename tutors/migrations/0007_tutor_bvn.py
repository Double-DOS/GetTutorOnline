# Generated by Django 3.0.5 on 2020-10-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0006_auto_20201025_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='bvn',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
