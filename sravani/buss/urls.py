# urls.py

from django.urls import path
from .views import signup,user_login,index,user_logout,create_assignment, assignment_list, submit_assignment, view_submissions, update_feedback

urlpatterns = [
    path('a',index, name='home'),
    path('login/',user_login, name='login'),
    # path('signup/', signup, name='signup'),
    path('signup_success/', signup, name='signup_success'),
    path('logout/',user_logout, name='logout'),
    path('create_assignment/', create_assignment, name='create_assignment'),
    path('assignment_list/', assignment_list, name='assignment_list'),
    path('submit_assignment/<int:assignment_id>/', submit_assignment, name='submit_assignment'),
    path('view_submissions/<int:assignment_id>/', view_submissions, name='view_submissions'),
    path('update_feedback/<int:submission_id>/', update_feedback, name='update_feedback'),

    
]
