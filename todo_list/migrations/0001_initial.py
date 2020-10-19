# Generated by Django 3.1 on 2020-08-31 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('description', models.CharField(max_length=100)),
                ('progress', models.BooleanField(default=False)),
                (
                    'page_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='todo_list.page'
                    ),
                ),
            ],
        ),
    ]