from rest import views
from django.urls import path


urlpatterns = [
    path('tasks', views.task_list),
    path('tasks/<int:pk>', views.task_detail),
    path('tasks/<int:pk>/subtasks', views.subtasks),
]
