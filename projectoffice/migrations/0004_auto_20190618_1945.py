# Generated by Django 2.2.1 on 2019-06-18 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectoffice', '0003_auto_20190613_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='comm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='projectoffice.CustomerCommChannel'),
        ),
        migrations.AlterField(
            model_name='customeradditionalattribute',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_aditional_info', to='projectoffice.Customer'),
        ),
        migrations.AlterField(
            model_name='customercommchannel',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_comm_channel', to='projectoffice.Customer'),
        ),
        migrations.AlterField(
            model_name='customerlegalinfo',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_legal_info', to='projectoffice.Customer'),
        ),
        migrations.AlterField(
            model_name='email',
            name='comm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='projectoffice.CustomerCommChannel'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='comm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='projectoffice.CustomerCommChannel'),
        ),
    ]