# Generated by Django 4.2.7 on 2023-11-19 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_redirect', models.URLField()),
                ('link_encurtado', models.CharField(max_length=5)),
            ],
        ),
    ]
