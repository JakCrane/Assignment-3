# Generated by Django 3.2.18 on 2023-03-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custapp', '0002_auto_20230322_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
