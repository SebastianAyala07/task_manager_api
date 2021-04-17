from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

import json
from datetime import datetime, date, timedelta

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import force_authenticate

from .models import Task

URL_TASK_CREATE = '/api/tasks/'
URL_TASKS_LIST = '/api/tasks/list/'


class TaskTest(TestCase):
    """ Test section for Task model """

    def setUp(self):
        self.client = APIClient()
        self.user_test = User.objects.create_user(
            username='admintest', password='passtest'
        )

    def test_create_task(self):
        self.client.login(username='admintest', password='passtest')
        data = {
            'title': 'Task Test (Do math work)',
            'description': 'Do math work',
            'is_completed': False,
            'deadline': (
                date.today() + timedelta(days=16)
            )
        }
        response = self.client.post(URL_TASK_CREATE, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_task_error_auth(self):
        data = {
            'title': 'Task Test',
            'description': 'Brush my teeth',
            'deadline': (
                date.today() + timedelta(days=16)
            )
        }
        response = self.client.post(URL_TASK_CREATE, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_task_error_data(self):
        self.client.login(username='admintest', password='passtest')
        data = {
            'title': 'Task Test',
            'deadline': (
                date.today() + timedelta(days=16)
            )
        }
        response = self.client.post(URL_TASK_CREATE, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_task_error_auth(self):
        response = self.client.get(URL_TASKS_LIST)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_task(self):
        self.client.login(username='admintest', password='passtest')
        response = self.client.get(URL_TASKS_LIST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_my_task(self):
        self.client.login(username='admintest', password='passtest')
        data = {
            'title': 'Task Test (Do math work)',
            'description': 'Do math work',
            'deadline': (
                date.today() + timedelta(days=16)
            )
        }
        self.client.post(URL_TASK_CREATE, data, format='json')
        response = self.client.get(URL_TASKS_LIST)
        result = json.loads(response.content)
        for task in result['results']:
            self.assertEqual(task['owner'], self.user_test)
