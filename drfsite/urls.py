"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib import admin
from women.views import *
from rest_framework import routers

# class MyCustomRouter(routers.SimpleRouter):
#     routers = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-detail',
#             detail=False,
#             initkwargs={'suffix': 'list'}
#         ),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]
# #router = routers.DefaultRouter() # это пакетный роутер так прописывается
# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls)),
    path('api/v1/women/', WomenAPIList.as_view()), #- маршруты без ViewSet-ов
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIDestroy.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view())
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})), - маршруты с ViuwSet=ами, но без роутеров
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'}))

]
