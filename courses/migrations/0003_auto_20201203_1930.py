# Generated by Django 3.1.3 on 2020-12-03 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_auto_20201127_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='ToBeCovered',
        ),
        migrations.RemoveField(
            model_name='course',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='course',
            name='videos',
        ),
        migrations.AddField(
            model_name='review',
            name='instructor',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor_reviewed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewed_by',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reviewed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='VideoRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoname', models.CharField(max_length=100)),
                ('videosrc', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('course', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
