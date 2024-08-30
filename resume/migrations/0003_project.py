# Generated by Django 5.0.7 on 2024-08-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('github_path', models.CharField(max_length=100)),
                ('is_online', models.BooleanField(default=False)),
                ('site_path', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
