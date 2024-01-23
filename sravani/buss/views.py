# myapp/views.py

from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import*

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Don't save the user yet
#             user_type = form.cleaned_data['user_type']

#             if user_type == 'admin':
#                 user.is_staff = True
#                 user.is_superuser = True
#             # elif user_type == 'seller':
#             #     user.is_staff = True
#             elif user_type == 'principal':
#                 user.is_superuser = True
#             elif user_type == 'teacher':
#                 user.is_staff = True

#             user.save()
#             return redirect('login')

#             # login(request, user)
#             # return redirect('signup_success')
#     else:
#         form = SignUpForm()

#     return render(request, 'signup.html', {'form': form})

def signup_success(request):
    return render(request, 'signup_success.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Assignment, Submission
from .forms import AssignmentForm, SubmissionForm

def get_teacher_or_none(user):
    try:
        return user.teacher
    except AttributeError:
        return None

def get_student_or_none(user):
    try:
        return user.student
    except Student.DoesNotExist:
        return None


@login_required
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            teacher = get_teacher_or_none(request.user)
            
            if teacher:
                assignment.teacher = teacher
                assignment.save()
                return redirect('assignment_list')
            else:
                # Handle the case where the user is not a teacher
                return render(request, 'not_teacher.html')
    else:
        form = AssignmentForm()
    
    return render(request, 'create_assignment.html', {'form': form})

@login_required
def assignment_list(request):
    teacher = get_teacher_or_none(request.user)
    if teacher:
        assignments = Assignment.objects.filter(teacher=teacher)
        return render(request, 'assignment_list.html', {'assignments': assignments})
    else:
        # Handle the case where the user is not a teacher
        return render(request, 'not_teacher.html')

@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = get_student_or_none(request.user)
            submission.save()
            return redirect('assignment_list')
    else:
        form = SubmissionForm()
    
    return render(request, 'submit_assignment.html', {'form': form, 'assignment': assignment})

@login_required
def view_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    teacher = get_teacher_or_none(request.user)
    if teacher and assignment.teacher == teacher:
        submissions = Submission.objects.filter(assignment=assignment)
        return render(request, 'view_submissions.html', {'assignment': assignment, 'submissions': submissions})
    else:
        # Handle the case where the user is not the teacher who created the assignment
        return render(request, 'not_teacher.html')

@login_required
def update_feedback(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('view_submissions', assignment_id=submission.assignment.id)
    else:
        form = SubmissionForm(instance=submission)
    
    return render(request, 'update_feedback.html', {'form': form, 'submission': submission})
