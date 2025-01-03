from django.shortcuts import redirect, render
from django.core import serializers

from portfolio.forms import (
    PortfolioPieceForm,
    SingleImageElementForm,
)
from portfolio.models import ImageElement, PortfolioPiece, ProjectTag


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
    form.fields["img"].widget.attrs = {"id": f"id_img_{counter}"}
    context = {"image_form": form, "counter": counter}
    return render(request, "portfolio/components/image_element.html", context)

def create_portfolio_piece(request):
    tags = ProjectTag.objects.all()
    data = serializers.serialize("json", tags)

    portfolio_form = PortfolioPieceForm()
    image_element = SingleImageElementForm()

    if request.method == "POST":
        portfolio_form = PortfolioPieceForm(request.POST, request.FILES)
        image_element = SingleImageElementForm(request.POST, request.FILES)

        if portfolio_form.is_valid():
            portfolio_piece = portfolio_form.save()
            for i in range(len(request.FILES.getlist("img"))):
                ImageElement.objects.create(
                    portfolio_piece=portfolio_piece,
                    img=request.FILES.getlist("img")[i],
                    caption=request.POST.getlist("caption")[i],
                    order=request.POST.getlist("order")[i],
                )

            return redirect("portfolio_work", pk=portfolio_piece.pk)


    context = {"portfolio_form": portfolio_form, "image_form": image_element, "data": data}
    return render(request, "portfolio/create_portfolio_piece.html", context)
