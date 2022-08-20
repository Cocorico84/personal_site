from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("blog/", include("blog.urls")),
    path("auth/", include("rest_framework.urls")),
    path("login/", views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("account/", include('django.contrib.auth.urls'), name='account'),
    # path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    # path("game/", include("detective.urls")),
    # path('user/', include('users.urls')),
]
