#coding : utf-8
"""mshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mysite.urls import router as fish_router 
from mysite import views
#from rest_framework import routers
#from .views import CarouselImgViewSet
#from .views import BulletInViewSet

#router = routers.DefaultRouter()
#router.register(r'carouselimg', views.CarouselImgViewSet)
#router.register(r'bulletin', views.BulletInViewSet)

urlpatterns = [
    url(r'^(\d*)$', views.index),
    url(r'^cart/$', views.cart),
    url(r'^product/(\d+)$', views.product, name='product-url'),
    url(r'^additem/(\d+)/(\d+)/(\d+)/$', views.add_to_cart, name='additem-url'),
    url(r'^removeitem/(\d+)/$', views.remove_from_cart, name='removeitem-url'),
    url(r'^order/$', views.order),
    url(r'^myorders/$', views.my_orders),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment/(\d+)/$', views.payment),
    url(r'^done/$', views.payment_done),
    url(r'^canceled/$', views.payment_canceled),
    url(r'^myorders/$', views.my_orders),
    url(r'^api/',include(fish_router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#router = routers.DefaultRouter()
#router.register(r'carouselimg', views.CarouselImgViewSet)
#router.register(r'bulletin', views.BulletInViewSet)
