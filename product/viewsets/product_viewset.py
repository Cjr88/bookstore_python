from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"results": serializer.data})