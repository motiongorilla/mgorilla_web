# Generated by Django 5.1.3 on 2025-01-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_imageelement_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageelement',
            name='temp',
            field=models.BooleanField(default=True),
        ),
    ]