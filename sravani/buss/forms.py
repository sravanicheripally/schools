# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('principal', 'principal'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label='User Type')
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'user_type']
        labels = {'email': 'Email'}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from .models import Subject, Teacher, Assignment, Student, Submission

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subjects_taught']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'subject', 'teacher']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'roll_number']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['assignment', 'student', 'answer', 'status', 'feedback']
