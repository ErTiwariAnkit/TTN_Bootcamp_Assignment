from django.urls import path
from . import views
urlpatterns = [
    path('',views.logout_page,name='mylogout')
]
