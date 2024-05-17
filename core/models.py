from django.db import models



# Create your models here.
class Student(models.Model):
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   date_of_birth = models.DateField()
   admission_no = models.CharField(max_length=30,unique=True)
class Teacher(models.Model):
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   tsc_no = models.CharField(max_length=30)

class Exam(models.Model):
    exam_name = models.CharField(max_length=30)
    exam_date = models.DateField()
    exam_code = models.CharField(max_length=30)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)


class Account(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    fee_paid = models.DecimalField(max_digits=10, decimal_places=2)
    fee_balance = models.DecimalField(max_digits=10, decimal_places=2)