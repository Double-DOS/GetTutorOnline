# Generated by Django 3.0.5 on 2020-10-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0004_auto_20201028_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorrequest',
            name='isRejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutorrequest',
            name='purpose_of_rejection',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
