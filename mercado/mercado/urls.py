from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs do app vendas
    path('', include('vendas.urls')),
]
