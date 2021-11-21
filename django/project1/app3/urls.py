from django.urls import path
from app3 import views

urlpatterns = [
    path("function1/",views.function1),
    path("function2/",views.function2),
    path("template/",views.template)

]