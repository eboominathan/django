from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html',{'posts':posts})

def post_page(request, slug) -> HttpResponse:
   post =  Posts.objects.get(slug=slug)    
   return render(request, 'posts/post_page.html', {'post':post})


