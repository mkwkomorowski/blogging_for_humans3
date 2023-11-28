"""
URLs for blogging_for_humans_3.
"""
from django.urls import url

from . import views

urlpatterns = [
    url(r"^abcd", views.return_first_model_if_exists),
]
