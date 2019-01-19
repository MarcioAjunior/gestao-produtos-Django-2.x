from django.contrib import admin
from django.urls import path, include
from produtos import urls as urls_produtos
from home import urls as urls_home
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
      path('produtos/', include(urls_produtos)),
       path('', include(urls_home)),
         path('login/',auth_views.LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
