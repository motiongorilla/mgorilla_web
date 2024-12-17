from django.contrib import admin

from portfolio.models import PortfolioPiece, ProjectTag

# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    # changing how article model looks at the admin panel.
    list_display = ("title", "status",)
    list_filter = ("tags", "status",)
    search_fields = ("title", "description", "tags", "status",)
    ordering = ("tags",)


admin.site.register(PortfolioPiece, PortfolioAdmin)
admin.site.register(ProjectTag)
