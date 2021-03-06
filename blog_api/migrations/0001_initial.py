# Generated by Django 4.0rc1 on 2021-12-22 04:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_api', '0005_user_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(upload_to='video/%y')),
                ('video_title', models.CharField(max_length=100)),
                ('video_description', models.TextField(blank=True, max_length=1500)),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('privacy', models.CharField(default='public', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_api.user')),
            ],
        ),
    ]
