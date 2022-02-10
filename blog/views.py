from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView,DetailView
# Create your views here.

class all_blogsListView(ListView):
    queryset = Blog.objects.all().order_by('-date')
    template_name = 'blog/all_blogs.html'
    context_object_name = 'blogs'
    paginate_by = 3


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:]
    # blogs = blogs[:len(blogs)-1]
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})