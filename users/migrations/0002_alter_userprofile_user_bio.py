# Generated by Django 3.2 on 2022-02-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_bio',
            field=models.CharField(max_length=2500, verbose_name='Biography'),
        ),
    ]
