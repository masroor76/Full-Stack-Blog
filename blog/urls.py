from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list),
    path('<slug:slug>/', post_detail)
]