# Generated by Django 2.2.4 on 2019-08-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]