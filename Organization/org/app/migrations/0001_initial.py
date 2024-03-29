# Generated by Django 2.2.1 on 2019-06-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAddress',
            fields=[
                ('add_id', models.IntegerField(primary_key=True, serialize=False)),
                ('com_id', models.CharField(max_length=32)),
                ('add_type', models.CharField(blank=True, max_length=20, null=True)),
                ('add_address_line1', models.CharField(blank=True, max_length=40, null=True)),
                ('add_addres_line2', models.CharField(blank=True, max_length=40, null=True)),
                ('add_city', models.CharField(blank=True, max_length=20, null=True)),
                ('add_state', models.CharField(blank=True, max_length=20, null=True)),
                ('add_country', models.CharField(blank=True, max_length=20, null=True)),
                ('add_pin', models.CharField(blank=True, max_length=10, null=True)),
                ('add_updated_on', models.DateTimeField(blank=True, null=True)),
                ('add_updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblAditionalAttribute',
            fields=[
                ('addinfo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('addinfo_attr', models.CharField(max_length=20)),
                ('addinfo_value', models.CharField(max_length=20)),
                ('addinfo_updated_on', models.DateTimeField(blank=True, null=True)),
                ('addinfo_updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_aditional_attribute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCommChannel',
            fields=[
                ('com_id', models.IntegerField(primary_key=True, serialize=False)),
                ('org_id', models.CharField(max_length=32)),
                ('com_type', models.CharField(max_length=40)),
                ('com_updated_on', models.DateTimeField(blank=True, null=True)),
                ('com_updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_comm_channel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblEmail',
            fields=[
                ('eml_id', models.IntegerField(primary_key=True, serialize=False)),
                ('com_id', models.CharField(max_length=32)),
                ('eml_address', models.CharField(max_length=40)),
                ('eml_updated_on', models.DateTimeField(blank=True, null=True)),
                ('eml_updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_email',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLegalInfo',
            fields=[
                ('legalinfo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('org_id', models.CharField(max_length=32)),
                ('legalinfo_type', models.CharField(max_length=30)),
                ('legalinfo_value', models.CharField(blank=True, max_length=100, null=True)),
                ('legalinfo_updated_on', models.DateTimeField(blank=True, null=True)),
                ('legalinfo_updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_legal_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblPhone',
            fields=[
                ('ph_id', models.IntegerField(primary_key=True, serialize=False)),
                ('com_id', models.CharField(max_length=32)),
                ('ph_isd_code', models.CharField(blank=True, max_length=10, null=True)),
                ('ph_std_code', models.CharField(blank=True, max_length=10, null=True)),
                ('ph_no', models.CharField(max_length=15)),
                ('ph_updated_on', models.DateTimeField(blank=True, null=True)),
                ('ph_updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_phone',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblOrganization',
            fields=[
                ('org_id', models.IntegerField(primary_key=True, serialize=False)),
                ('org_name', models.CharField(max_length=50)),
                ('org_level', models.CharField(max_length=20)),
                ('org_country', models.CharField(max_length=20)),
                ('org_code', models.CharField(max_length=20)),
                ('org_currency', models.CharField(max_length=20)),
                ('org_language', models.CharField(max_length=20)),
                ('parent_org_id', models.CharField(blank=True, max_length=20, null=True)),
                ('org_updated_on', models.DateTimeField(blank=True, null=True)),
                ('org_updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_organization',
            },
        ),
    ]
