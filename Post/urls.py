from django.urls import path, include
from .views import HomeView,PostDetailsView,CreatePostView
urlpatterns = [
    path("",HomeView.as_view(), name="Home"),
    path("article/<int:pk>",PostDetailsView.as_view() ,name="post_details_path"),
    path("create post/",CreatePostView.as_view(),name="createpost")
]