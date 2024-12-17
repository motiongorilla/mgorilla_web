from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from articles.models import Article


class ArticlesListView(ListView):
    template_name = "articles/blog_list.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.order_by("-created_at")


class LandingView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by("-created_at")
        return context


class ReadArticleView(TemplateView):
    template_name = "articles/layouts/article_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs.get("pk")
        article = Article.objects.get(pk=article_id)
        context['article'] = article
        context['article_content_html'] = article.get_content_as_html()
        return context


class DashboardArticleListView(LoginRequiredMixin, ListView):
    template_name = "articles/dashboard.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "articles/create_article.html"
    model = Article
    fields = ["title", "status", "content", "post_summary"]
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "articles/update_article.html"
    model = Article
    fields = ["title", "status", "content", "post_summary"]
    success_url = reverse_lazy("dashboard")
    context_object_name = "article"

    def test_func(self):
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "articles/delete_article.html"
    model = Article
    success_url = reverse_lazy("dashboard")
    context_object_name = "article"

    def test_func(self):
        return self.request.user == self.get_object().creator
