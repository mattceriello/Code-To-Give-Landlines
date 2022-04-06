from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
import nltk
import text2emotion as te

nltk.download('omw-1.4')


# Create your views here.

# def home(request):
#     return HttpResponse('<h1> Callodine Blog </h1>')


# def about(request):
#     return HttpResponse('<h1> Profile - Baju </h1>')

# posts = [
#     {
#         'author':'Baju',
#         'username':'isribalaji',
#         'date_posted':'December 30, 2021',
#         'content':'Forcing ourselves or others to always be positive can be harmful to our well-being and our relationships. There is a better approach.'
#     },
#     {
#         'author':'Abhishek',
#         'username':'abhishekp',
#         'date_posted':'December 28, 2021',
#         'content':'I have 3 big surprises for you this new year, the first of which I will announce on Jan 1st. But can you guess without any hint from me'
#     },
#     {
#         'author':'Priya',
#         'username':'priyavarman',
#         'date_posted':'December 29, 2021',
#         'content':'What is your favorite movie of all time?'
#     }
# ]

## We are going to create class based views which will handle many things on their own at the backend. Previously, we have used function based views.


posts = Post.objects.all()

@login_required
def home(request):
    context = {
        'post' : posts,
        'title' : 'Happy Eve!!'
    }

    return render(request, 'microblog/home.html', context)

## paginate_by = <no_of_post> is enough to paginate the web page. As we are using class based views it reduces a lot of code.

class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'microblog/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'microblog/userpost.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        current_user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(username = current_user).order_by('-date_posted')

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        emotion  = te.get_emotion(kwargs['object'].content + kwargs['object'].title )
        emotion = {k: v*100 for k, v in sorted(emotion.items(), key=lambda item: item[1], reverse=True)}
        context["emotion"] = emotion
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user.first_name
        form.instance.username = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user.first_name
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        current_post = self.get_object()
        if(current_post.username == self.request.user):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        current_post = self.get_object()
        if(current_post.username == self.request.user):
            return True
        else:
            return False

@login_required
def about(request):
    context = {
        'title':'isribalaji'
    }
    return render(request, 'microblog/about.html', context)

@login_required
def happydays(request):
    context = {
        'title':'Happy Days'
    }
    return render(request, 'microblog/happydays.html', context)

def error_404(request, *args, **argv):
        data = {}
        return render(request,'microblog/error404.html', data)

def error_500(request, *args, **argv):
        data = {}
        return render(request,'microblog/error500.html', data)