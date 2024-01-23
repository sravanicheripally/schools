from django.contrib import admin
from .models import Subject, Teacher, Assignment, Student, Submission,User

admin.site.register(User)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_subjects_taught']

    def get_subjects_taught(self, obj):
        return ", ".join([subject.name for subject in obj.subjects_taught.all()])
    get_subjects_taught.short_description = 'Subjects Taught'

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'subject', 'teacher', 'created_data']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'roll_number']

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'submitted_date', 'status', 'feedback']
