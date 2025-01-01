from django.utils.deprecation import MiddlewareMixin

from portfolio.models import ImageElement


class DeleteTemporaryImagesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == "GET" and request.headers.get('x-requested-with') != 'XMLHttpRequest':
            ImageElement.objects.filter(temp=True).delete()
