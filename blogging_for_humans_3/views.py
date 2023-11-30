from . import models
from django.http import HttpResponse


def return_first_model_if_exists(request):
    queryset = models.Model123.objects.all()
    list_of_models = list(queryset)
    result = list_of_models[0].id if list_of_models else 'abcd'
    return HttpResponse(str(result))
