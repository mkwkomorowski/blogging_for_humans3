from . import models
from django.http import HttpResponse


def return_first_model_if_exists(request):
    queryset = models.Model123.objects.all()
    result = list(queryset)[0] or 'abcd'
    return HttpResponse("result: " + (str(result)))
