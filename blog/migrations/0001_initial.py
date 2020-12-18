# Generated by Django 3.1.4 on 2020-12-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('link', models.URLField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
