
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('exam/',include('exam.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
