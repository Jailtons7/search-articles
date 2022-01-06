from rest_framework import viewsets

from api.models import TblArtigoPublicado
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
