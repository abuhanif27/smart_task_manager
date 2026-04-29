from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path("delete/<int:id>/", views.delete_task, name="delete_task"),
    path("edit/<int:id>/", views.edit_task, name="edit_task"),
    path("update/<int:id>/", views.update_task, name="update_task"),
    path("search/", views.search_tasks, name="search_tasks"),
    path("filter/", views.filter_tasks, name="filter_tasks"),
]