from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('chat/', include('chat.api.urls', namespace='chat')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
         path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', include('post.urls'), name='posts'),
]
