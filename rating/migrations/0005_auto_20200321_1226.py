# Generated by Django 3.0.4 on 2020-03-21 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_auto_20200321_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='pub_date',
            new_name='post_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_title',
            new_name='title',
        ),
    ]
