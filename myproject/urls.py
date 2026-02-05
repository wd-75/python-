from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name='home'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('student_list/', student_list, name='student_list'),
]
