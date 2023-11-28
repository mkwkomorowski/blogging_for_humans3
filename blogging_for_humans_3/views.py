from . import models
from django.http import HttpResponse


def render_something_from_model(request):
    queryset = models.Model123.objects.all()
    result = list(queryset)[0] or 'abcd'
    return HttpResponse("result: " + (str(result)))
