import re

import markdown
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from articles.managers import UserProfileManager

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)


class UserProfile(AbstractUser):
    email = models.EmailField("email address", max_length=255, unique=True)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def article_count(self):
        return self.articles.count()

    @property
    def written_words(self):
        return self.articles.aggregate(models.Sum("word_count"))["word_count__sum"] or 0


class Article(models.Model):
    title: models.CharField = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    thumbnail = models.URLField(max_length=500, default="")
    post_summary = models.TextField(blank=True, default="")
    tags = models.ManyToManyField("Tag")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUS,
        default="draft",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="articles")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_content_as_html(self):
        return markdown.markdown(self.content, extensions=["markdown.extensions.fenced_code"])


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name