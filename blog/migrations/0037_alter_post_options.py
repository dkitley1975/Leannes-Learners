# Generated by Django 3.2 on 2022-03-13 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_alter_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
