# Generated by Django 3.2.5 on 2023-08-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_backlinkhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlink',
            name='first_crawled_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]