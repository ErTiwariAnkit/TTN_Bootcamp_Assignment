from django.urls import path
from . import views
urlpatterns = [
    path('',views.set_home_page,name='home')
]
