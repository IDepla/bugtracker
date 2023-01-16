from django.contrib.auth.models import AnonymousUser

from django.test import RequestFactory, TestCase

from .views import CreateBug, OpenBugs

from .models import User


class CreateBugTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="secret",
        )
        return super().setUp()

    def test_access_anonymous(self):
        """
        access open bug from anonymous shall fail
        """
        request = self.factory.get("/open/")

        request.user = AnonymousUser()

        response = OpenBugs.as_view()(request)

        # it shall redirect
        self.assertEqual(response.status_code, 302)

    def test_access_auth(self):
        """
        access open bug from authenticated shall success
        """
        request = self.factory.get("/open/")

        request.user = self.user

        response = OpenBugs.as_view()(request)

        # it shall redirect
        self.assertEqual(response.status_code, 200)

    def test_create_anonymous(self):
        """
        create a bug from anonymous shall fail
        """
        request = self.factory.get("/bug/create/")

        request.user = AnonymousUser()

        response = CreateBug.as_view()(request)

        # it shall redirect
        self.assertEqual(response.status_code, 302)

    