from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self,Student):
            return True
        return False
    @property
    def is_teacher(self):
        if hasattr(self,Teacher):
            return True
        return False

class  Dept(models.Model):
    id=models.CharField(max_length=25,primary_key='True')
    name=models.CharField(max_length=50)

class Course(models.Model):
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    id=models.CharField(max_length=25,primary_key='True')
    name=models.CharField(max_length=50)
    shortname=models.CharField(max_length=10)

class  Class(models.Model):
    courses=models.ManyToManyField(Course)
    id=models.CharField(max_length=25,primary_key='True')
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    section=models.CharField(max_length=10)
    Sem=models.IntegerField()

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
    id=models.CharField(max_length=25,primary_key='True')
    name=models.CharField(max_length=25)
    sex=models.CharField(max_length=25,choices=sex_choice, default='Female')
    DOB=models.DateField(default='1999-26-12')

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    id=models.CharField(max_length=25,primary_key='True')
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    sex=models.CharField(max_length=25,choices=sex_choice,default='Female')
    DOB=models.DateField(default='1999-26-12')

class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'class_id', 'teacher'),)

    def __str__(self):
        cl = Class.objects.get(id=self.class_id_id)
        cr = Course.objects.get(id=self.course_id)
        te = Teacher.objects.get(id=self.teacher_id)
        return '%s : %s : %s' % (te.name, cr.shortname, cl)




