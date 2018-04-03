import uuid

from django.conf import settings
from django.shortcuts import render


def index(request):
    context = {
        'is_debug': settings.DEBUG,
        'force_static_serving': settings.FORCE_STATIC_FILE_SERVING
    }
    if settings.DEBUG:
        context['js_version'] = str(uuid.uuid4())
    return render(request, 'index.html', context=context)
