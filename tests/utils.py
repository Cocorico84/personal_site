from rest_framework.test import APITestCase

from blog.models import Article
from users.models import User


class CustomTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="Toto")
        self.article = Article.objects.create(
            title="Test",
            subject="Hello world",
            author=self.user,
        )
