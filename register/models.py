from django.db import models

class admin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class faculty(models.Model):
        name = models.CharField(max_length=30,null=True,blank=True)
        password = models.CharField(max_length=10,null=True,blank=True)
class meta:
        db_table:"register_faculty"
         
class facultysignup(models.Model):

    factid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=10)

    password = models.CharField(max_length=10)
    assbatch = models.CharField(max_length=10)
class meta:
    db_table:"register_facultysignup" 
class student(models.Model):
    stdid = models.IntegerField(primary_key=True)
    admno = models.IntegerField(null=True,blank=True)
    name =  models.CharField(max_length=30,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    admdate = models.DateField(null=True,blank=True)
    guardian = models.CharField(max_length=10,null=True,blank=True)
    batch = models.CharField(max_length=10,null=True,blank=True)
    email = models.CharField(max_length=1,null=True,blank=True)
    password = models.CharField(max_length=10,null=True,blank=True)
class meta:
    db_table:"register_studentsignup" 

class studentattend(models.Model):

    
     date = models.DateField(max_length=5)
     stdid = models.IntegerField (null=True,blank=True)
     name =  models.CharField(max_length=30)
     hour1status = models.CharField(max_length=5)
     hour2status = models.CharField(max_length=5)
     hour3status = models.CharField(max_length=5)
     hour4status = models.CharField(max_length=5)
class meta:
    db_table:"register_studentattend"
class factleave(models.Model):
    name=models.CharField(max_length=30)
    fromdate=models.DateField(max_length=5)
    todate= models.DateField(max_length=5)
    reason=models.CharField(max_length=5)
    
class meta:
    db_table:"register_factleave"

class studleave(models.Model):
    name=models.CharField(max_length=30)
    fromdate=models.DateField(max_length=5)
    todate= models.DateField(max_length=5)
    reason=models.CharField(max_length=5)
    
class meta:
    db_table:"register_studleave"    
class studentmark(models.Model):

     stdid= models.IntegerField(null=True,blank=True)
     name =  models.CharField(max_length=30)
     assessmentno = models.IntegerField(null=True,blank=True)
     sub1mark =models.IntegerField(null=True,blank=True)
     sub2mark =models.IntegerField(null=True,blank=True)
     sub3mark =models.IntegerField(null=True,blank=True)
     percentage=models.IntegerField(null=True,blank=True)
class meta:
    db_table:"register_studentmark" 
class facultyattendence(models.Model):

    date = models.DateField(max_length=5)
    factid = models.IntegerField(null=True,blank=True)
    name =  models.CharField(max_length=30)
    hours1status = models.CharField(max_length=5)
    hours2status = models.CharField(max_length=5)
    hours3status = models.CharField(max_length=5)
    hours4status = models.CharField(max_length=5)
class meta:
    db_table:"register_facultyattend"     







    


# Create your models here.
