from django.urls import path
from . import views
from .views import PostView,PostDetailView,PostCreateView,PostUpdateView, PostDeleteView, UserPost

urlpatterns = [
    # path('', views.home, name='miniblog'),
    path('', PostView.as_view(), name='miniblog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='individual_post'),
    path('user/<str:username>/', UserPost.as_view(), name='individual_user'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='new_post'),
    path('about/', views.about, name='about'),
    path('buffalo-days/', views.happydays, name='happydays'),
]