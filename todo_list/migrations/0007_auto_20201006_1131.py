# Generated by Django 3.1 on 2020-10-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_auto_20200917_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(),
        ),
    ]
