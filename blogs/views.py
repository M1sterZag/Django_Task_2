from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    return render(request, "blogs/index.html")


def blogs(request):
    blogs = BlogPost.objects.order_by("date_added")
    context = { "blogs": blogs }
    return render(request, "blogs/blogs.html", context)


def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = { "blog": blog}
    return render(request, "blogs/blog.html", context)