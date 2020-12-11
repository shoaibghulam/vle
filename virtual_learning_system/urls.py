from django.contrib import admin
from django.urls import path , include
#for images
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include('clientside.urls')),
    path('superadmin/', include('superadmin.urls')),
    path('clientside/', include('clientside.urls')),
    path('teacherpannel/', include('teacher.urls')),

    

    



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)