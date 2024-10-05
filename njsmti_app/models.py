from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    stud_mob = models.CharField(max_length=15)
    parents_mob = models.CharField(max_length=15)
    email = models.CharField(max_length=75)
    dob = models.DateField()  # Changed to ISO format
    birth_place = models.CharField(max_length=50)
    category = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=40)
    college = models.CharField(max_length=50)
    course = models.CharField(max_length=40)
    semester = models.CharField(max_length=29)
    # Renamed to avoid conflict with the reserved word 'class'
    class_name = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email
    
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    dob = models.DateField()
    birthplace = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.email
    
class Diary(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    message = models.TextField()
    
    def __str__(self):
        return self.email

class Query(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    query = models.TextField()
    
    def __str__(self):
        return self.email

class ReplyQuery(models.Model):
    email = models.EmailField()
    question = models.TextField()
    query = models.TextField()
    
    def __str__(self):
        return self.email

class AllFaculty(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    dob = models.DateField()
    birthplace = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email

class Material(models.Model):
    Topic = models.CharField(max_length=80)
    semester = models.CharField(max_length=50)
    link = models.TextField()


class Director(models.Model):
    email = models.CharField(max_length=80, default="njsmticampus@gmail.com")
    password = models.CharField(max_length=24, default="director@12")
    
    def __str__(self):
        return self.email