from django.db import models

# Create your models here.

class User14(models.Model):
    user_name=models.CharField(max_length=20) 
    pwd=models.CharField(max_length=30)
    class Meta:
        db_table="User14"

class User15(models.Model):
    user_name=models.CharField(max_length=20) 
    pwd=models.CharField(max_length=30)
    class Meta:
        db_table="User15"

class User20(models.Model):
    name=models.CharField(max_length=20) 
    age=models.IntegerField()
    reason=models.CharField(max_length=30) 
    blood_group=models.CharField(max_length=10) 
    blood_volume=models.IntegerField()
    class Meta:
        db_table="User20"

class User21(models.Model):
    name=models.CharField(max_length=20) 
    age=models.IntegerField()
    reason=models.CharField(max_length=30) 
    blood_group=models.CharField(max_length=10) 
    blood_volume=models.IntegerField()
    class Meta:
        db_table="User21"

class User23(models.Model):
    blood_group=models.CharField(max_length=50)
    blood=models.IntegerField()
    class Meta:
        db_table="User23"

class User24(models.Model):
    blood_group=models.CharField(max_length=50)
    blood=models.IntegerField()
    class Meta:
        db_table="User24"

class User28(models.Model):
    blood_group1=models.IntegerField()
    blood_group2=models.IntegerField()
    class Meta:
        db_table="User28"

class User29(models.Model):
    blood_group=models.CharField(max_length=50)
    blood=models.IntegerField()
    class Meta:
        db_table="User29"

class User30(models.Model):
    blood_groupA1=models.IntegerField()
    blood_groupB1=models.IntegerField()
    blood_groupO1=models.IntegerField()
    blood_groupAB1=models.IntegerField()
    blood_groupA2=models.IntegerField()
    blood_groupB2=models.IntegerField()
    blood_groupO2=models.IntegerField()
    blood_groupAB2=models.IntegerField()
    total_request=models.IntegerField()
    total_blood_unit=models.IntegerField()
    approved_request=models.IntegerField()
    rejected_request=models.IntegerField()
    class Meta:
        db_table="User30"

class User31(models.Model):
    blood_group=models.CharField(max_length=50)
    blood_volume=models.IntegerField()
    class Meta:
        db_table="User31"

class User32(models.Model):
    blood_group=models.CharField(max_length=50)
    blood_volume=models.IntegerField()
    class Meta:
        db_table="User32"

class User33(models.Model):
    blood_groupA1=models.IntegerField()
    blood_groupB1=models.IntegerField()
    blood_groupO1=models.IntegerField()
    blood_groupAB1=models.IntegerField()
    blood_groupA2=models.IntegerField()
    blood_groupB2=models.IntegerField()
    blood_groupO2=models.IntegerField()
    blood_groupAB2=models.IntegerField()
    total_request=models.IntegerField()
    total_blood_unit=models.IntegerField()
    approved_request=models.IntegerField()
    rejected_request=models.IntegerField()
    class Meta:
        db_table="User33"

class User34(models.Model):
    name=models.CharField(max_length=20) 
    age=models.IntegerField()
    reason=models.CharField(max_length=30) 
    blood_group=models.CharField(max_length=10) 
    blood_volume=models.IntegerField()
    class Meta:
        db_table="User34"