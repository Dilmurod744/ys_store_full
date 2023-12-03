from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FunctionalSuggesterFilterBackend, \
    FilteringFilterBackend, OrderingFilterBackend, CompoundSearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from elasticsearch_dsl import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.documents import ProductDocument
from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, ProductDocumentSerializer


# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    # search_fields = ('name',)


class ProductDocumentViewSet(DocumentViewSet):
    document = ProductDocument
    filter_backends = [SearchFilterBackend]
    serializer_class = ProductDocumentSerializer
    search_fields = ('name', 'description',)
