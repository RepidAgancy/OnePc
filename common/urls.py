from django.urls import path

from common import views

urlpatterns = [
    path('about-us/', views.AboutUsApiView.as_view(), name='about-us'),
    path('ads-list/', views.AdvertisementApiView.as_view(), name='advertisement'),
    path('contact-us/', views.ContactUsApiView.as_view(), name='contact-us'),
]