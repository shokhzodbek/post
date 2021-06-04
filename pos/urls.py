from django.urls import path
from .views import Postpage


urlpatterns = [
    path('',Postpage.as_view(),name="posts")
]
