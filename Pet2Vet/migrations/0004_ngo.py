# Generated by Django 2.0.13 on 2019-04-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet2Vet', '0003_adoptform_donateform_firstaid_vet'),
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]