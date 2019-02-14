import uuid

from django.conf import settings
from django.shortcuts import render

from cms.models.configs import AppConfig


def index(request):
    context = {
        'title': 'MiNi CMS',
        'is_debug': settings.DEBUG,
        'force_static_serving': settings.FORCE_STATIC_FILE_SERVING
    }

    app_config = AppConfig.objects.last()
    if app_config:
        context['title'] = app_config.browser_title
    if settings.DEBUG:
        context['js_version'] = str(uuid.uuid4())
    return render(request, 'index.html', context=context)

def admin(request):
    context = {
        'title': 'MiNi CMS',
        'is_debug': settings.DEBUG,
        'force_static_serving': settings.FORCE_STATIC_FILE_SERVING
    }

    app_config = AppConfig.objects.last()
    if app_config:
        context['title'] = app_config.browser_title
    if settings.DEBUG:
        context['js_version'] = str(uuid.uuid4())
    return render(request, 'admin.html', context=context)
