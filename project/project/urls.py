
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('api/admin/', admin.site.urls),
    url(r"^api/v1/",include('customer.routes')),
    url(r"^api/v1/",include('user.routes')),
    url(r"^api/v1/",include('dealer.routes')),
    url(r"^api/v1/",include('location.routes')),
    url(r"^api/v1/",include('bottler.routes')),
]
