from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("<slug:slug>", views.book_detail, name="book-detail"),
    # path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]