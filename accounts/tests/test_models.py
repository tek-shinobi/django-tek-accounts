# mypy: ignore-errors
import pytest
from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db


class TestUserManager:
    def test_create_superuser(self, superuser_factory):
        user_created = superuser_factory()
        user = get_user_model()
        user_from_db = user.objects.get(id=user_created.id)
        assert user_from_db.id == user_created.id, "Should be equal"
        assert user_created.id == 1, "Should be 1"
        assert user_from_db.is_active is True
        assert user_from_db.is_admin is True
        assert user_from_db.is_staff is True
        assert user_from_db.has_perm("foo") is True
        assert user_from_db.has_module_perms("foo") is True
        assert user_from_db.get_full_name() == user_created.email
        assert user_from_db.get_short_name() == user_created.email
        assert str(user_from_db) == user_created.email

    def test_create_user(self, user_factory):
        user_created = user_factory()
        user = get_user_model()
        user_from_db = user.objects.get(id=user_created.id)
        assert user_from_db.id == user_created.id, "Should be equal"
        assert user_created.id == 1, "Should be 1"
        assert user_from_db.is_active is True
        assert user_from_db.is_admin is False
        assert user_from_db.is_staff is True

    def test_manager_create_user(self):
        user = get_user_model()
        user_created = user.objects.create_staff_user(email="m@m.com", password="user")
        user_from_db = user.objects.get(id=user_created.id)
        assert user_from_db.id == user_created.id, "Should be equal"
        assert user_created.id == 1, "Should be 1"
        assert user_from_db.is_active is True, "Should be True"
        assert user_from_db.is_admin is False, "Should be False"
        assert user_from_db.is_staff is True, "Should be True"

    def test_manager_create_superuser(self):
        user = get_user_model()
        user_created = user.objects.create_superuser(email="m@m.com", password="admin")
        user_from_db = user.objects.get(id=user_created.id)
        assert user_from_db.id == user_created.id, "Should be equal"
        assert user_created.id == 1, "Should be 1"
        assert user_from_db.is_active is True, "Should be True"
        assert user_from_db.is_admin is True, "Should be True"
        assert user_from_db.is_staff is True, "Should be True"

    def test_manager_create_user_error(self):
        user = get_user_model()
        with pytest.raises(ValueError, match="Users must have an email address"):
            user.objects.create_superuser(email=None, password="admin")
        with pytest.raises(ValueError, match="Users must have a password"):
            user.objects.create_superuser(email="m@m.com")
