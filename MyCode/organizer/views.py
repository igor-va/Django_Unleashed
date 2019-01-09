from django.http.response import Http404, HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response, render

from .models import Startup, Tag


def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render_to_response('organizer/tag_detail.html', {'tag': tag})


def startup_list(request):
    return render(request, 'organizer/startup_list.html',
                  {'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup': startup})