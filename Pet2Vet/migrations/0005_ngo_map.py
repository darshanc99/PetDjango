# Generated by Django 2.0.13 on 2019-04-06 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet2Vet', '0004_ngo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='map',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
