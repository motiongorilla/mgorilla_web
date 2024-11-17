from django.shortcuts import redirect, render

from app.forms import CreateArticleForm
from app.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})


def create_article(request):
    if request.method == "POST":
        # data is submitted
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_article = Article(
                title=form_data.get("title"),
                status=form_data.get("status"),
                content=form_data.get("content"),
                word_count=form_data.get("word_count"),
                twitter_post=form_data.get("twitter_post"),
            )
            new_article.save()
            return redirect("home")
    else:
        # HTML should be returned
        form = CreateArticleForm()
    return render(request, "app/create_article.html", {"form": form})
