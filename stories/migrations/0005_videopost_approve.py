# Generated by Django 3.0.4 on 2020-03-26 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200323_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='videopost',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
