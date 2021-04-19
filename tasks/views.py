from django.shortcuts import redirect

from rest_framework import status, filters, permissions, viewsets
from rest_framework.generics import ListAPIView

from .models import Task
from .permissions import IsOwner
from .serializers import TaskSerializer

class ListTaskByUser(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['description']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.tasks_by_owner(user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    http_method_names = ['post', 'put', 'patch', 'delete']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def redirect_documentation(request):
    return redirect('schema-swagger-ui')
