# Generated by Django 4.0.4 on 2022-05-09 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_rename_listing_category_id_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category_link',
        ),
    ]
