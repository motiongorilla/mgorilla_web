from django.urls import path

from articles.views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticlesListView,
    ArticleUpdateView,
    DashboardArticleListView,
    LandingView,
    ReadArticleView,
)

urlpatterns = [
    path("", LandingView.as_view(), name="index"),
    path("posts/", ArticlesListView.as_view(), name="posts"),
    path("articles/", DashboardArticleListView.as_view(), name="dashboard"),
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("articles/<int:pk>/", ReadArticleView.as_view(), name="read_article"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="update_article"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_article"),
]
