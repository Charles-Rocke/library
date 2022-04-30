from django.urls import path
from .views import BookListView

# urls here
urlpatterns = [
    path("", BookListView.as_view(), name = "home"),
]