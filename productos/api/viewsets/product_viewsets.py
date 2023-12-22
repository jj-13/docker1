from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from base.utils import validate_data
from productos.api.serializers.product_serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    parser_classes = (JSONParser, MultiPartParser)
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request, *args, **kwargs):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        print(request.data)
        data = validate_data(request.data, 'image')
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            data = validate_data(request.data, 'image', True)
            product_serializer = self.serializer_class(self.get_queryset(pk), data=data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message': 'Producto actualizado'}, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe producto con esos datos'}, status=status.HTTP_404_NOT_FOUND)







