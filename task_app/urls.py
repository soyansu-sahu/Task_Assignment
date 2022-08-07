from django.urls import path, include
from task_app import views
from . views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # custom_urls
    path('', views.root),
    # path('task_list/',TaskList.as_view(), name="task-list"),
    # path('task_update/<str:pk>/',UpdateTask.as_view(), name="task-update"),
    # path('create_task/',CreateTask.as_view(), name="create-task"),
    # path('create_team/',CreateTeam.as_view(),name="create-team"),
    # path('api-token-auth/', UserAuthToken.as_view()),
    path('task_list/',views.taskList),
    path('task_list/<int:id>',views.taskDetails),
    path('team_list',views.teamList)

]

# urlpatterns =  format_suffix_patterns(urlpatterns)


