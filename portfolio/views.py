from django.shortcuts import redirect, render

from portfolio.forms import (
    PortfolioPieceForm,
    SingleImageElementForm,
)
from portfolio.models import ImageElement, PortfolioPiece


def portfolio_list(request):
    works = PortfolioPiece.objects.order_by("-published_at")
    context = {"works": works}
    return render(request, "portfolio/portfolio_list.html", context=context)

def portfolio_work(request, **kwargs):
    work_id = kwargs.get("pk")
    work = PortfolioPiece.objects.get(pk=work_id)
    context = {"portoflio_work": work}
    return render(request, "portfolio/portfolio_work.html", context=context)

def image_element(request):
    counter = int(request.GET.get("element_order", 0))

    form = SingleImageElementForm(initial={"order":counter, "temp":True})
    context = {"image_form": form}
    return render(request, "portfolio/components/image_element.html", context)

def image_detail(request, pk):
    image = ImageElement.objects.get(pk=pk)

    if request.method == "POST":
        form = SingleImageElementForm(request.POST, request.FILES, instance=image)
        form = form.save()
        return redirect("image_detail", pk=form.pk)
    else:
        form = SingleImageElementForm(instance=image, initial={"temp":True})

    context = {"image": image, "form": form}
    return render(request, "portfolio/components/image_detail.html", context)

def create_portfolio_piece(request):
    portfolio_form = PortfolioPieceForm()
    image_element = SingleImageElementForm()

    if request.method == "POST":
        portfolio_form = PortfolioPieceForm(request.POST, request.FILES)
        image_element = SingleImageElementForm(request.POST, request.FILES)

        if "img" in request.FILES and image_element.is_valid():
            image = image_element.save()
            return redirect("image_detail", pk=image.pk)

        if portfolio_form.is_valid():
            portfolio_piece = portfolio_form.save()

            # Update ImageElements with the foreign key of the PortfolioPiece
            image_elements = ImageElement.objects.filter(portfolio_piece__isnull=True)
            for image in image_elements:
                image.portfolio_piece = portfolio_piece
                image.temp = False
                image.save()

            return redirect("portfolio_work", pk=portfolio_piece.pk)


    context = {"portfolio_form": portfolio_form, "image_form": image_element}
    return render(request, "portfolio/create_portfolio_piece.html", context)
