# Generated by Django 3.2 on 2022-02-08 05:49

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_rename_body_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(verbose_name='Biography')),
                ('bio_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255)),
                ('alt_tag', models.CharField(max_length=200, verbose_name='Describe the image for the blind')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
