from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    queryset=Post.objects.order_by("-Created_on")
    template_name="home.html"

class PostDetailsView(DetailView):
    model = Post
    template_name="post_details.html"

class CreatePostView(CreateView):
    model = Post
    form_class=PostForm
    template_name="createpost.html"






