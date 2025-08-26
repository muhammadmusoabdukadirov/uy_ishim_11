from django.shortcuts import render, get_object_or_404
from .models import Advertisement, Announcement, Comment
from django.http import HttpRequest, HttpResponse
from django.contrib import messages

def index(request):
    advertisements = Advertisement.objects.all() 
    announcements = Announcement.objects.all()

    context = {
        "advertisements": advertisements,
        "announcements": announcements,
        "title": "Asosiy saxifa"
    }
    return render(request, 'app/index.html', context=context)


def new_by_category(request, category_id: int):
    advertisements = Advertisement.objects.all()
    category = get_object_or_404(Advertisement, pk=category_id)
    announcements = Announcement.objects.filter(author=category, published=True)
    context = {
        "advertisements": advertisements,
        "announcements": announcements,
        "title": category.title,
    }
    return render(request, "app/index.html", context)


def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    context = {
        'announcement': announcement
    }
    return render(request, 'app/announcement_detail.html', context)