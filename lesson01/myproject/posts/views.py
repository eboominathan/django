from django.shortcuts import render
from .models import Posts

# Create your views here.
def post_list(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html',{'posts':posts})


