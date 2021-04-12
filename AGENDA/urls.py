"""AGENDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# lembrar de instalar o pillow: pip install pillow
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # para importação de imagens
from django.conf.urls.static import static  # para importação de imagens

urlpatterns = [
    path('', include('contatos.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    # por causa desse caminho que fica accounts/cadastro, etc. O app contato não fica pq o caminho é '' (vazio).
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # para importação de imagens
# -> agora tem que configurar o MEDIA_URL e MEDIA_ROOT no settings.py
