from django.urls import path

from .views import ArticleDetail, ArticleList

urlpatterns = [
    # path("articles/", ArticleViewSet.as_view({'get': 'list', 'post': 'create'}))
    path("articles/", ArticleList.as_view(), name="blog"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="article-detail"),
]
