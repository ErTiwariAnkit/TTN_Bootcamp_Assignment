from django.urls import path
from . import views
urlpatterns = [
    path('function2/',views.function1,name='app2')
]
