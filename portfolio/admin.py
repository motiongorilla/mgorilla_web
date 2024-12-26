from django.contrib import admin

from portfolio.models import ImageElement, PortfolioPiece, ProjectTag, TextElement, VideoElement


class ImageElementInline(admin.TabularInline):
    model = ImageElement
    extra = 1


class VideoElementInline(admin.TabularInline):
    model = VideoElement
    extra = 1


class TextElementInline(admin.TabularInline):
    model = TextElement
    extra = 1


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "published_at", "created_at",)
    list_filter = ("tags", "status",)
    search_fields = ("title", "description", "tags", "status", "published_at", "created_at",)
    ordering = ("tags", "published_at", "created_at",)
    readonly_fields = ("published_at", )
    inlines = [ImageElementInline, VideoElementInline, TextElementInline]


admin.site.register(PortfolioPiece, PortfolioAdmin)
admin.site.register(ProjectTag)
admin.site.register(ImageElement)
admin.site.register(VideoElement)
admin.site.register(TextElement)
