"""
blogging_for_humans_3 Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins import PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType


plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^blogging_for_humans_3/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
    }


class BloggingForHumans3Config(AppConfig):
    """
    Configuration for the blogging_for_humans_3 Django application.
    """

    name = 'blogging_for_humans_3'

    # plugin_app = {
    #     PluginURLs.CONFIG: {
    #         ProjectType.LMS: {
    #             PluginURLs.NAMESPACE: name,
    #             PluginURLs.REGEX: "^blogging_for_humans_3/",
    #             PluginURLs.RELATIVE_PATH: "urls",
    #         }
    #     },
    # }
