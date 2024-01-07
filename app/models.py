from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    def __str__(self):
        return self.dname

class Emp(models.Model):
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    emp_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.ename

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    high_sal=models.IntegerField()
    low_sal=models.IntegerField()

   

class Bonus(models.Model):
    grade=models.IntegerField()
    bonus=models.IntegerField(primary_key=True)




