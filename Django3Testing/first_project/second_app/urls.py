from django.urls import path
from second_app.views import index2

urlpatterns = [
    path('',index2,name="index2"),
]