# Generated by Django 3.2 on 2022-01-08 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0017_rename_pass_plus_passplus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passplus',
            name='background_image_alt_tag',
        ),
    ]
