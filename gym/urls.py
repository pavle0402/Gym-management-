from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('members_list/', views.MembersListView.as_view(), name='members_list'),
    path('register_member/', views.RegisterMemberView.as_view(), name='register_member'),
    path('members_list/<int:pk>/delete', views.MemberDeleteView.as_view(), name='delete_member'),
    path('members_list/<int:pk>/edit', views.MemberUpdateView.as_view(), name='edit_member'),
    path('trainers_list/', views.TrainerListView.as_view(), name='trainers_list'),
    path('register_trainer/', views.RegisterTrainerView.as_view(), name='register_trainer'),
    path('trainers_list/<int:pk>/delete', views.TrainerDeleteView.as_view(), name='delete_trainer'),
    path('trainers_list/<int:pk>/edit', views.TrainerEditView.as_view(), name='edit_trainer'),
    path('subtract_session/<int:member_id>', views.subtract_sessions, name='sessions'),
    path('trainer_details/<int:trainer_id>', views.trainer_details, name="trainer_details"),

]