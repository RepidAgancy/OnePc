from django.db.models import Q, Count
from django.contrib.postgres.aggregates import ArrayAgg

from rest_framework import generics, permissions, response, status, views
import django_filters.rest_framework

from product import models, serializers, filters


class ProductListApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()


class ProductDetailApiView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ProductDetailSerializer
    queryset = models.Product.objects.all()
    lookup_field = 'uuid'


class ProductSimilarListApiView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ProductListSerializer

    def get(self, request, uuid):
        try: 
            product = models.Product.objects.get(uuid = uuid)

        except models.Product.DoesNotExist:
            return response.Response(
                {"error": "Product not found."}, 
                status=status.HTTP_404_NOT_FOUND
            )

        similar_products = models.Product.objects.filter(
            Q(category=product.category) | Q(brand=product.brand)
            ).exclude(uuid=product.uuid)
        
        serializer = self.get_serializer(similar_products, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class ProductCategoryListApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.CategoryListSerializer
    queryset = models.CategoryProduct.objects.all()


class ProductCategoryIscommonListApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.CategoryListSerializer
    queryset = models.CategoryProduct.objects.filter(is_common=True)


class ProductBrandListApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.BrandListSerializer
    queryset = models.BrandProduct.objects.all()


class ProductNewApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all().order_by('-created_at')


class ProductTopApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.filter(is_top=True)


class ProductCommonApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.filter(is_common=True)


class ProductByCategoryApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ProductListSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = filters.ProductFilter

    def get_queryset(self):
        category_uuid = self.kwargs.get('uuid')  
        queryset = models.Product.objects.filter(category__uuid=category_uuid)
        return queryset
    

class InfoNameByCategoryAPIView(views.APIView):
    def get(self, request, uuid):
        try:
            category = models.CategoryProduct.objects.get(uuid=uuid)

            valid_info = (
                models.ProductComponents.objects.filter(product__category=category)
                .values('info_name') 
                .annotate(
                    info_text_count=Count('info_text', distinct=True),  # Count distinct info_text
                    info_text_list=ArrayAgg('info_text', distinct=True),  # Collect all unique info_text
                )
                .filter(info_text_count__gt=2)  
            )

            result = [
                {
                    "info_name": item['info_name'],
                    "info_text": item['info_text_list'],
                    "is_valid": True
                }
                for item in valid_info
            ]

            return response.Response({"valid_info": result}, status=200)
        except models.CategoryProduct.DoesNotExist:
            return response.Response({"error": "Category not found"}, status=404)
        

class OrderCreateApiView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        product_list_ids = request.data.get('product_list_ids', [])
        qauntity_list = request.data.get('quantity_list', [])

        if not product_list_ids or not qauntity_list:
            return response.Response({"message":"Products must be given and order quantity must be"}, status=status.HTTP_400_BAD_REQUEST)
        if len(product_list_ids) != len(qauntity_list): 
            return response.Response({"message":"Lengths must be equal with product and quantity"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            delivery_form = serializer.save()  # Save the delivery form

            for product_id, quantity in zip(product_list_ids, qauntity_list):
                try:
                    product = models.Product.objects.get(id=product_id)
                except models.Product.DoesNotExist:
                    return response.Response({"error": f"Product with ID {product_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)

                # Create the OrderProduct entry
                models.OrderProduct.objects.create(
                    delivery_form=delivery_form,
                    product=product,
                    quantity=quantity
                )

            return response.Response(
                {
                    "message": "Order created successfully",
                    "delivery_form": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

