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
    thumbnail = models.ImageField(null=True, blank=True, upload_to="media/portfolio_thumbs")
    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS,
        default="personal",
    )


class ProjectTag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name
