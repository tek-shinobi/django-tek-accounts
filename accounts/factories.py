import factory
from faker import Factory as FakerFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

faker = FakerFactory.create()
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    staff = True
    admin = False
    password = factory.LazyFunction(
        lambda: make_password("user")
    )  # all users have user as password


class SuperuserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    staff = True
    admin = True
    password = factory.LazyFunction(
        lambda: make_password("admin")
    )  # all superusers have admin as password
