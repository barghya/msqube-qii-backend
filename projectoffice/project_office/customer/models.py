# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblAddress(models.Model):
    #id = models.AutoField(unique=True)
    add_id = models.CharField(primary_key=True, max_length=32)
    com_id = models.CharField(max_length=32)
    add_type = models.CharField(max_length=20, blank=True, null=True)
    add_address_line1 = models.CharField(max_length=40, blank=True, null=True)
    add_addres_line2 = models.CharField(max_length=40, blank=True, null=True)
    add_city = models.CharField(max_length=20, blank=True, null=True)
    add_state = models.CharField(max_length=20, blank=True, null=True)
    add_country = models.CharField(max_length=20, blank=True, null=True)
    add_pin = models.CharField(max_length=10, blank=True, null=True)
    add_updated_on = models.DateTimeField(blank=True, null=True)
    add_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_address'




class TblCustomer(models.Model):
   # id = models.AutoField(unique=True)
    customer_id = models.CharField(primary_key=True, max_length=32)
    customer_name = models.CharField(max_length=30)
    customer_code = models.CharField(max_length=30, blank=True, null=True)
    customer_type = models.CharField(max_length=30, blank=True, null=True)
    customer_tag = models.CharField(max_length=30)
    customer_updated_on = models.DateTimeField(blank=True, null=True)
    customer_updated_by = models.CharField(max_length=20, blank=True, null=True)
	
    class Meta:
        managed = False
        db_table = 'tbl_customer'


class TblCustomerAditionalAttribute(models.Model):
    #id = models.AutoField(unique=True)
    addinfo_id = models.CharField(primary_key=True, max_length=32)
    customer_id = models.CharField(max_length=32)
    addinfo_attr = models.CharField(max_length=20)
    addinfo_value = models.CharField(max_length=20)
    addinfo_updated_on = models.DateTimeField(blank=True, null=True)
    addinfo_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer_aditional_attribute'

class TblCommChannel(models.Model):
    #id = models.AutoField(unique=True)
    com_id = models.CharField(primary_key=True, max_length=32)
    cutomer_id = models.ForeignKey(TblCustomer, related_name='cust_ref', on_delete=models.CASCADE)
    com_type = models.CharField(max_length=30)
    com_updated_on = models.DateTimeField(blank=True, null=True)
    com_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_comm_channel'

class TblEmail(models.Model):
    #id = models.AutoField(unique=True)
    eml_id = models.CharField(primary_key=True, max_length=32)
    com_id = models.CharField(max_length=32)
    eml_address = models.CharField(max_length=40)
    eml_updated_on = models.DateTimeField(blank=True, null=True)
    eml_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_email'


class TblLegalInfo(models.Model):
    #id = models.AutoField(unique=True)
    legalinfo_id = models.CharField(primary_key=True, max_length=32)
    customer_id = models.CharField(max_length=32)
    legalinfo_type = models.CharField(max_length=30)
    legalinfo_value = models.CharField(max_length=100, blank=True, null=True)
    legalinfo_updated_on = models.DateTimeField(blank=True, null=True)
    legalinfo_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_legal_info'


class TblPhone(models.Model):
   # id = models.AutoField(unique=True)
    ph_id = models.CharField(primary_key=True, max_length=32)
    com_id = models.CharField(max_length=32)
    ph_isd_code = models.CharField(max_length=20, blank=True, null=True)
    ph_std_code = models.CharField(max_length=20, blank=True, null=True)
    ph_no = models.CharField(max_length=15)
    ph_updated_on = models.DateTimeField(blank=True, null=True)
    ph_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_phone'


class TblProject(models.Model):
   # id = models.AutoField(unique=True)
    project_id = models.CharField(primary_key=True, max_length=32)
    customer_id = models.CharField(max_length=32)
    project_name = models.CharField(max_length=30)
    project_code = models.CharField(max_length=30)
    project_type = models.CharField(max_length=30)
    project_updated_on = models.DateTimeField(blank=True, null=True)
    project_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_project'


class TblProjectAttributes(models.Model):
    #id = models.AutoField(unique=True)
    proj_att_id = models.CharField(primary_key=True, max_length=32)
    project_id = models.CharField(max_length=32)
    proj_attribute = models.CharField(max_length=30, blank=True, null=True)
    proj_value = models.CharField(max_length=30, blank=True, null=True)
    proj_att_updated_on = models.DateTimeField(blank=True, null=True)
    proj_att_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_project_attributes'
