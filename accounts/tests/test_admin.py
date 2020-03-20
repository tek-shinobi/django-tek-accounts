# mypy: ignore-errors
import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model

User = get_user_model()
from .. import admin

pytestmark = pytest.mark.django_db


class TestUserAdmin:
    def test_admin(self, superuser_factory):
        user_created = superuser_factory()
        admin_site = AdminSite()
        user_admin = admin.UserAdmin(model=User, admin_site=admin_site)
        result = user_admin.model.objects.get(id=user_created.id).email
        assert result == user_created.email, "Should be the same email"
