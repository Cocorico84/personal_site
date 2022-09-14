from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer

# class ArticleViewSet(ModelViewSet):
#     renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)

#     template_name = "article.html"
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # permission_classes = [IsAuthenticated]


class ArticleList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "article.html"

    def get(self, request):
        queryset = Article.objects.order_by("-created_date")
        return Response({"articles": queryset})


class ArticleDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "article_detail.html"

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        # serializer = ArticleSerializer(article)
        # return Response(serializer.data)
        return Response({"article": article})

    # def patch(self, request, pk):
    #     article = self.get_object(pk)
    #     serializer = ArticleSerializer(article, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"article": serializer.data})
    #     return Response(status=HTTP_404_NOT_FOUND)
