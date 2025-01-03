from django.urls import path

from portfolio.views import create_portfolio_piece, image_element, portfolio_list, portfolio_work

urlpatterns =[
    path("", portfolio_list, name="portfolio"),
    path("create_portfolio/", create_portfolio_piece, name="create_portfolio"),
    path("work/<int:pk>/", portfolio_work, name="portfolio_work"),
    path("htmx/image-element-form/", image_element, name="add_image_element"),
]
