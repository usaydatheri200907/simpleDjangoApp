from django.contrib import admin
from django.urls import path
from myapp import views  # Import your views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_view, name='hello'),  # Example path
    path('', views.home_view, name='home'),  # Add a path for the root URL
]
