# Generated by Django 3.1 on 2020-09-17 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0005_auto_20200917_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='page_id',
            new_name='page',
        ),
    ]