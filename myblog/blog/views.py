from django.shortcuts import render
from django.conf import settings
from blog.models import *


# Create your views here.

def global_settings(request):
    return {
        "SITE_NAME": settings.SITE_NAME, "SITE_DESC": settings.SITE_DESC
    }


def index(request):
    blogs = BlogArticle.objects.all()
    return render(request, "index.html", locals())


def about(request):
    try:
        author = BlogUser.objects.first()
    except Exception as e:
        print e
    return render(request, "about.html", locals())


def archive(request):
    sorted_blogs = BlogArticle.objects.all()
    return render(request, "archive.html", locals())


def blog(request):
    blog_id = request.GET.get('blog_id')
    blog = BlogArticle.objects.get(id=blog_id)
    return render(request, "blog.html", locals())


def category(request):
    return render(request, "category.html", locals())


def friend(request):
    return render(request, "friend.html")


def message(request):
    return render(request, "message.html")


def not_found(request):
    return render(request, "not_found.html")
