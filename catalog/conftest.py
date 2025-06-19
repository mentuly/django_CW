import os

import django
import pytest


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog.settings")
django.setup()

from rest_framework.test import APIClient


@pytest.fixture
def user():
    return django.contrib.auth.models.User.objects.create_user(
        username="testusertestusertestuser", password="password_test_user"
    )


@pytest.fixture
def api_client():
    return APIClient()
