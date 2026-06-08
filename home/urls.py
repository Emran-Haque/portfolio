from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('education/', views.EducationView.as_view(), name='education'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('competitive-programming/', views.CompetitiveProgrammingView.as_view(), name='competitive-programming'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
