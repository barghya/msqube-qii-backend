# Generated by Django 2.2.1 on 2019-06-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190618_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialmaster',
            name='id',
        ),
        migrations.RemoveField(
            model_name='materialunit',
            name='id',
        ),
        migrations.AlterField(
            model_name='materialmaster',
            name='mate_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='materialunit',
            name='mat_unit_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
