# Generated by Django 2.2.2 on 2019-06-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectoffice', '0002_customerlegalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
