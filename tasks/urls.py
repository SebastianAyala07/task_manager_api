from django.urls import include, re_path, path

from task_manager.urls import router
from . import views

app_name="tasks_app"

router.register(r'api/tasks', views.TaskViewSet)

urlpatterns = [
    path(
        'api/tasks/list/',
        views.ListTaskByUser.as_view(),
        name='tasks-by-user'
    )
]