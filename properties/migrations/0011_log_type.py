# Generated by Django 3.2.6 on 2021-08-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_filter_unique filter constraint'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]