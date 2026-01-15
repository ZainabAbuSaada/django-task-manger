from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),

]

