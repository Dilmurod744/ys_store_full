from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework.serializers import ModelSerializer

from apps.documents import ProductDocument
from apps.models import Category, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument
        fields = [
            'id',
            'name',
            'description',
        ]

