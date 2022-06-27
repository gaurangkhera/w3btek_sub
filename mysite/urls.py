from django.urls import path
from .views import home, product, register, contact, success, detail,about


urlpatterns=[
    path('', home.as_view(), name="home"),
    path('product/', product.as_view(), name='product'),
    path('success/', success, name='success'),
    path('about/', about, name='about'),
    path('product/<int:pk>', detail.as_view(), name="detail"),
    path('contact/', contact.as_view(), name='contact'),
    path('register/', register.as_view(), name='register'),
]