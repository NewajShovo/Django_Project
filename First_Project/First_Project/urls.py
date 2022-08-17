from django.contrib import admin
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home, name='home'),
    path('customers/',include('first_app.urls')),
    # path('contact/',views.contact, name='contact'),
    # path('about/', views.about, name='about'),
]
