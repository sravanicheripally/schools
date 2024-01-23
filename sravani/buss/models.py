from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('principal', 'principal'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )


class Subject(models.Model):
   name = models.CharField(max_length=100)
   def __str__(self):
       return self.name

class Teacher(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'user_type': "teacher"})
   subjects_taught = models.ManyToManyField(Subject)
   def __str__(self):
       return self.user.username

class Assignment(models.Model):
   title = models.CharField(max_length=255)
   description = models.TextField()
   due_date = models.DateField()
   created_data=models.DateTimeField(auto_now_add=True)
   subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
   def __str__(self):
       return self.title

class Student(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'user_type': "student"})
   roll_number = models.CharField(max_length=20)
   def __str__(self):
       return self.user.username
       
class Submission(models.Model):
   assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   submitted_date = models.DateTimeField(auto_now_add=True)
   answer = models.TextField()
   status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
   feedback = models.TextField(blank=True, null=True)
   def __str__(self):
       return f"{self.student.user.username} - {self.assignment.title} - {self.status}"

