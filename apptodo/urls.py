from django.urls import path
from apptodo import views


urlpatterns = [
    path('', views.todoHome, name='todo-home'),
    path('delete_task/<int:id>/', views.deleteTask, name='delete-task'),
    path('done_task/<int:id>/', views.doneTask, name='done-task'),
    path('delete_all_done/', views.deleteAllDone, name='delete-all-done'),
]