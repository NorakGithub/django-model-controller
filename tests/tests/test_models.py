from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase


class TestModel(TestCase):
    def setUp(self):
        # self.company_name = "Company name test"
        # self.user = User.objects.create_user(username="username_test", password="password_test")
        pass

    def test_model_controller_should_not_created_without_required_fields(self):
        # with self.assertRaises(IntegrityError):
        #     Company.objects.create(name=self.company_name)
        pass

    def test_model_controller_should_able_to_create_instance(self):
        # Company.objects.create(name=self.company_name, created_user=self.user, updated_user=self.user)
        # assert True
        pass

    def test_model_should_have_model_controller_fields(self):
        # company = Company.objects.create(
        #     name=self.company_name, created_user=self.user, updated_user=self.user
        # )
        # assert company.name == self.company_name
        # assert company.created_user == self.user
        # assert company.updated_user == self.user
        pass
