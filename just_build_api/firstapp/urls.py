from django.urls import path
from . import views


urlpatterns = [path('helloworld', views.hello_world), path('hellotest', views.HelloTest.as_view())]