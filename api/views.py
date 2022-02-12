from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import views, viewsets, status
from rest_framework.response import Response

from api.models import (
    TblArtigoPublicado, TblArtigoPublicadoAreaConhecimento, TblArtigoPublicadoPalavrasChave,
    TblServidores
)
from api.serializers import ArtigoPublicadoSerializer


class ArtigosPublicadosViews(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArtigoPublicadoSerializer
    queryset = TblArtigoPublicado.objects.all()

    def get_queryset(self):
        query = self.queryset
        filters = self.request.GET
        ano = filters.get('ano')
        if ano:
            query = query.filter(AnoPublicacaoArtigo__exact=ano)
        titulo = filters.get('titulo')
        if titulo:
            query = query.filter(CodTitulosArtigos__DscTitulosArtigos__icontains=titulo)
        autor = filters.get('autor')
        if autor:
            query = query.filter(CodServidor__NomServidor__icontains=autor)
        return query

    def retrieve(self, request, *args, **kwargs):
        article = get_object_or_404(TblArtigoPublicado, CodArtigoPublicado=self.kwargs['pk'])  # breakpoint here
        data = article.get_article_info()
        return Response(data=data, status=status.HTTP_200_OK)


class DashboardView(views.APIView):
    def get(self, request):
        articles_per_org = TblArtigoPublicado.articles_per_orgao()
        articles_per_grande_area = TblArtigoPublicadoAreaConhecimento.articles_per_grande_area()
        artcles_per_year = TblArtigoPublicado.articles_per_year()
        articles_per_author = TblArtigoPublicado.articles_per_author()
        servidores_per_ie = TblServidores.servidores_per_ie()
        professores_per_ie = TblServidores.professores_per_ie()
        return Response({
            'articles_per_org': articles_per_org,
            'articles_per_grande_area': articles_per_grande_area,
            'articles_per_year': artcles_per_year,
            'articles_per_author': articles_per_author,
            'servidores_per_ie': servidores_per_ie,
            'professores_per_ie': professores_per_ie,
        }, status=status.HTTP_200_OK)
