from django.urls import path

from portfolio.views import create_portfolio_piece, portfolio_list, portfolio_work

urlpatterns =[
    path("", portfolio_list, name="portfolio"),
    path("create_portfolio/", create_portfolio_piece, name="create_portfolio"),
    path("work/<int:pk>/", portfolio_work, name="portfolio_work"),
]
