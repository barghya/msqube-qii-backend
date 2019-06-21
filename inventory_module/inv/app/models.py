
from __future__ import unicode_literals
from django.db import models

class materialmaster(models.Model):
    mate_id=models.IntegerField(primary_key=True)
    mate_name=models.CharField(max_length=20)
    mate_code=models.CharField(max_length=20)
    mate_type=models.CharField(max_length=20)
    mate_desc=models.CharField(max_length=20)
    mate_updated_on=models.DateTimeField(auto_now_add=True)
    mate_updated_by=models.CharField(max_length=20)
    class Meta:
        db_table='tbl_material_master'

class materialunit(models.Model):
    mat_unit_id=models.IntegerField(primary_key=True)
    mate_id=models.ForeignKey(materialmaster,related_name='mat_unit',on_delete=models.CASCADE)
    mat_unit_type=models.CharField(max_length=20)
    mat_unit_updated_on=models.DateTimeField(auto_now_add=True)
    mat_unit_updated_by=models.CharField(max_length=20)
    class Meta:
        db_table='tbl_material_unit'