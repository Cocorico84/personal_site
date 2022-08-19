from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("blog/", include("blog.urls")),
    path("auth/", include("rest_framework.urls")),
    # path("game/", include("detective.urls")),
    # path('user/', include('users.urls')),
]
