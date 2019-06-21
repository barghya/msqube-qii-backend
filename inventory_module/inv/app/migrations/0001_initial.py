# Generated by Django 2.2.1 on 2019-06-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblConstSpec',
            fields=[
                ('const_spec_id', models.AutoField(primary_key=True, serialize=False)),
                ('const_spec_name', models.CharField(max_length=30)),
                ('const_spec_unit_value', models.IntegerField()),
                ('const_spec_unit', models.CharField(max_length=10)),
                ('const_spec_updated_on', models.TextField()),
                ('const_spec_updated_by', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tbl_const_spec',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblConstSpecMate',
            fields=[
                ('const_spec_mat_id', models.AutoField(primary_key=True, serialize=False)),
                ('const_spec_id', models.IntegerField()),
                ('mate_id', models.IntegerField()),
                ('const_spec_mate_quantity', models.IntegerField()),
                ('const_spec_mate_unit', models.CharField(max_length=20)),
                ('const_spec_mate_updated_on', models.TextField()),
                ('const_spec_mate_updated_by', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tbl_const_spec_mate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMarterialMaster',
            fields=[
                ('mate_id', models.AutoField(primary_key=True, serialize=False)),
                ('mate_name', models.CharField(max_length=40)),
                ('mate_code', models.CharField(max_length=20)),
                ('mate_type', models.CharField(max_length=30)),
                ('mate_desc', models.CharField(max_length=30)),
                ('mate_updated_on', models.TextField()),
                ('mate_updated_by', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tbl_marterial_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMaterialUnit',
            fields=[
                ('mate_unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('mate_id', models.IntegerField()),
                ('mate_unit_type', models.CharField(max_length=20)),
                ('mate_unit_updated_on', models.TextField()),
                ('mate_unit_updated_by', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tbl_material_unit',
                'managed': False,
            },
        ),
    ]
