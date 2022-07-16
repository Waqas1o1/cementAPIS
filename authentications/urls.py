from .views import *
from django.urls import path, include
from knox import views as knox_views
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()
routes.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('', include(routes.urls)),
    path('filterUsers/', UserFilter.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
