from django.db import models

# Create your models here.

class FirstLevel(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	midname = models.CharField(max_length=20)
	position = models.CharField(max_length=20)
	AceptanceDate = models.DateField()
	pay = models.IntegerField()

class SecondLevel(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	midname = models.CharField(max_length=20)
	position = models.CharField(max_length=20)
	AceptanceDate = models.DateField()
	pay = models.IntegerField()	
	had = models.ForeignKey(FirstLevel, on_delete = models.CASCADE, null = True)	

class ThirdLevel(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	midname = models.CharField(max_length=20)
	position = models.CharField(max_length=20)
	AceptanceDate = models.DateField()
	pay = models.IntegerField()	
	had = models.ForeignKey(SecondLevel, on_delete = models.CASCADE, null = True)	

class FourthLevel(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	midname = models.CharField(max_length=20)
	position = models.CharField(max_length=20)
	AceptanceDate = models.DateField()
	pay = models.IntegerField()	
	had = models.ForeignKey(ThirdLevel, on_delete = models.CASCADE, null = True)	

class FifthLevel(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	midname = models.CharField(max_length=20)
	position = models.CharField(max_length=20)
	AceptanceDate = models.DateField()
	pay = models.IntegerField()	
	had = models.ForeignKey(FourthLevel, on_delete = models.CASCADE, null = True)	