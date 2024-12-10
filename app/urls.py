from django.urls import path

from app.views import ArticleCreateView, ArticleDeleteView, ArticleListView, ArticleUpdateView, LandingView, ReadArticleView

urlpatterns = [
    path("", LandingView.as_view(), name="index"),
    path("articles/", ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("articles/<int:pk>/", ReadArticleView.as_view(), name="read_article"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="update_article"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_article"),
]
