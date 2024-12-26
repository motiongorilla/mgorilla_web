from django.shortcuts import redirect, render

from portfolio.forms import (
    ImageElementFormset,
    MultipleImageElementForm,
    PortfolioMediaElementFormset,
    PortfolioPieceForm,
    TextElementFormset,
    VideoElementFormset,
)
from portfolio.models import PortfolioPiece


def portfolio_list(request):
    works = PortfolioPiece.objects.order_by("-published_at")
    context = {"works": works}
    return render(request, "portfolio/portfolio_list.html", context=context)

def portfolio_work(request, **kwargs):
    work_id = kwargs.get("pk")
    work = PortfolioPiece.objects.get(pk=work_id)
    context = {"portoflio_work": work}
    return render(request, "portfolio/portfolio_work.html", context=context)

def create_portfolio_piece(request):
    if request.method == "POST":
        portfolio_form = PortfolioPieceForm(request.POST, request.FILES)

        multiple_images = MultipleImageElementForm(request.POST, request.FILES)
        image_formset = ImageElementFormset(request.POST, request.FILES, prefix="images")
        video_formset = VideoElementFormset(request.POST, request.FILES, prefix="videos")
        text_formset = TextElementFormset(request.POST, prefix="texts")

        if portfolio_form.is_valid():
            portfolio_piece = portfolio_form.save()

            if image_formset.is_valid():
                image_formset.instance = portfolio_piece
                image_formset.save()

            if video_formset.is_valid():
                video_formset.instance = portfolio_piece
                video_formset.save()

            if text_formset.is_valid():
                text_formset.instance = portfolio_piece
                text_formset.save()

            return redirect("portfolio_work", pk=portfolio_piece.pk)
    else:
        portfolio_form = PortfolioPieceForm()
        multiple_images = MultipleImageElementForm()
        image_formset = ImageElementFormset(prefix="images")
        video_formset = VideoElementFormset(prefix="videos")
        text_formset = TextElementFormset(prefix="texts")

    context = {"portfolio_form": portfolio_form,
               "multiple_images_form": multiple_images,
               "image_formset": image_formset,
               "video_formset": video_formset,
               "text_formset": text_formset}

    return render(request, "portfolio/create_portfolio_piece.html", context)
