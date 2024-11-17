import re

from django.contrib.auth.models import AbstractUser
from django.db import models

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progrss"),
    ("published", "published"),
)


class UserProfile(AbstractUser): ...


class Article(models.Model):
    title: models.CharField = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField(blank=True, default="")
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUS,
        default="draft",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", " ", self.content).replace("&nbsp;", " ")
        print(text)
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)

