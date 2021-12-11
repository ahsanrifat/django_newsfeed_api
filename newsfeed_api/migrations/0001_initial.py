# Generated by Django 4.0rc1 on 2021-12-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_api', '0004_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeedSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=900)),
                ('sources', models.CharField(max_length=900)),
                ('keywords', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth_api.user')),
            ],
            options={
                'db_table': 'custom_user_news_settings',
            },
        ),
    ]