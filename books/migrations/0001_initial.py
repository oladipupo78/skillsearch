# Generated by Django 3.1.4 on 2020-12-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/home-profile.jpg', upload_to='')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]