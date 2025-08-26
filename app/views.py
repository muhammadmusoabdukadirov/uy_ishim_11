from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsForm
from django.core.exceptions import PermissionDenied
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


def add_app(request: HttpRequest):
    if not request.user.is_staff:
        raise PermissionDenied
    
    if request.method == 'POST':
        if request.user.is_staff:
            form = NewsForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                news = form.save()
                messages.success(request, "Maqola muvaffaqiyatli qabul qilindi!")
                return redirect("announcement_detail", news.pk)
    else:
        form = NewsForm()
    context = {
        "form": form,
        "title": "Maqola qo‘shildi"
    }
    return render(request, "app/add_app.html", context)


def update_app(request, pk: int):
    if not request.user.is_staff:
        raise PermissionDenied

    app = get_object_or_404(Announcement, pk=pk)  # Advertisement emas, Announcement bo'lishi kerak
    if request.method == "POST":
        form = NewsForm(data=request.POST, files=request.FILES, instance=app)
        if form.is_valid():
            form.save()
            return redirect("announcement_detail", app.pk)
    else:
        form = NewsForm(instance=app)

    context = {
        "form": form,
        "title": "Maqola Yangilash"
    }
    return render(request, "app/add_app.html", context)

def delete_app(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == "POST":
        announcement.delete()
        return redirect("index")
    return redirect("index")
