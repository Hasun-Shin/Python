# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    shop_desc = models.CharField(max_length=100, blank=True, null=True)
    rest_date = models.CharField(max_length=100, blank=True, null=True)
    parking_info = models.CharField(max_length=100, blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'
    
    def __str__(self):
        return  str(self.shop_id) + '\t' +self.shop_name + '\t'+ self.shop_desc+ '\t'+ self.rest_date+ '\t'+ self.parking_info+ '\t'+ self.img_path+'<br>'
