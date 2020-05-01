from django.urls import path
from . import views
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
