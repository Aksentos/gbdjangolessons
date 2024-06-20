from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'), name='myapp'),
    path('les3/', include('myapp3.urls'), name='myapp3'),
    path('les4/', include('myapp4.urls'), name='myapp4'),
    # path('__debug__/', include("debug_toolbar.urls")),
    path('les6/', include('myapp6.urls')),
]
