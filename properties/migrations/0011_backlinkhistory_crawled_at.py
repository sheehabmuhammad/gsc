# Generated by Django 3.2.5 on 2023-08-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_backlink_first_crawled_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlinkhistory',
            name='crawled_at',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]