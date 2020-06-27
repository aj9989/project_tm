from django.urls import path
from .views import Index, TaskListView

urlpatterns = [
    path('', Index.as_view()),
    path('api', TaskListView.as_view())
]