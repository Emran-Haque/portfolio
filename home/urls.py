from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('competitive-programming/', views.competitive_programming, name='competitive_programming'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_list, name='blog_list'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
