from django.db import models

PROJECT_STATUS = (
    ("personal", "Personal"),
    ("exploration", "Exploration"),
    ("commercial", "Commecrial"),
)

class PortfolioPiece(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    tags = models.ManyToManyField("ProjectTag")
    thumbnail = models.ImageField(null=True, blank=True, upload_to="portfolio_thumbs/")
    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS,
        default="personal",
    )
    published_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


class ProjectTag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class PortfolioMediaElement(models.Model):
    ELEMENT_SELECTOR = (
        ("image", "Image"),
        ("video", "Video"),
        ("text", "Text"),
    )
    portfolio_piece = models.ForeignKey(PortfolioPiece, related_name="elements", on_delete=models.CASCADE)
    element_type = models.CharField(max_length=10, choices=ELEMENT_SELECTOR)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="portfolio_media/", blank=True, null=True)
    video = models.FileField(upload_to="portfolio_media/", blank=True, null=True)
    text = models.TextField(blank=True, default="")
    caption = models.CharField(max_length=150, blank=True, default="")

    def __str__(self):
        return f"{self.element_type} - {self.order}"


class ImageElement(models.Model):
    portfolio_piece = models.ForeignKey(PortfolioPiece, related_name="image_elements", on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="portfolio_media/")
    caption = models.CharField(max_length=150, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption

class TextElement(models.Model):
    portfolio_piece = models.ForeignKey(PortfolioPiece, related_name="text_elements", on_delete=models.CASCADE)
    text = models.TextField(blank=True, default="")

    def __str__(self):
        return self.text[:50]

class VideoElement(models.Model):
    portfolio_piece = models.ForeignKey(PortfolioPiece, related_name="video_elements", on_delete=models.CASCADE)
    video = models.FileField(upload_to="portfolio_media/")
    caption = models.CharField(max_length=150)

    def __str__(self):
        return self.caption
