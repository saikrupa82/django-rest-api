from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    # path('admin/', admin.site.urls),
    path('api/v1/', include('user.api_urls')),
    path('api/v1/', include('employee.api_urls')),
    path('api/v1/', include('poll.api_urls')),
    path('api/v1/category/', include('category.api_urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
