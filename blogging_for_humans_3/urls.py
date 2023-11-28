"""
URLs for blogging_for_humans_3.
"""
from django.urls import re_path, url  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

from . import views

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="blogging_for_humans_3/base.html")),
    url(r"^abcd", views.return_first_model_if_exists),
]
