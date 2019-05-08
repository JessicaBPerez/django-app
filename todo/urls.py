from django.urls import path
from . import views

urlpatterns = [
    path('', views.school_index),
    path('schools/', views.school_index, name='school_index'),
    path('professors/', views.professor_index, name='professor_index'),
    path('schools/<int:id>', views.school_show, name='school_show'),
    path('professors/<int:id>', views.professor_show, name='professor_show'),
    path('schools/new/', views.school_new, name='school_new'),
    path('professors/new/', views.professor_new, name='professor_new'),
    path('schools/<int:id>/edit', views.school_edit, name='school_edit'),
    path('professors/<int:id>/edit', views.professor_edit, name="professor_edit"),
    path('schools/<int:id>/delete', views.school_delete, name="school_delete"),
    path('professors/<int:id>/delete', views.professor_delete, name="professor_delete"),
]