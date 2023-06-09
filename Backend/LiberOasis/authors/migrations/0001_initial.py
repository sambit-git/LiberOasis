# Generated by Django 4.2.2 on 2023-06-09 20:56

import LiberOasis.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('bio', models.TextField()),
                ('country', models.CharField(max_length=128)),
                ('qualification', models.CharField(blank=True, max_length=128, null=True)),
                ('occupation', models.CharField(blank=True, max_length=128, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=LiberOasis.utilities.upload_to)),
            ],
        ),
    ]