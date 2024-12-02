from rest_framework import serializers
from product import models


class ProductListSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField(method_name='get_discount_price')
    image = serializers.SerializerMethodField(method_name='get_image')

    class Meta:
        model = models.Product
        fields = (
            'uuid', 'name', 'price', 'discount_price', 'discount', 'image'
        )

    def get_discount_price(self, obj):
        if obj.discount:
            return obj.price * obj.discount / 100

    def get_image(self, obj):
        if obj.product_image.exists(): 
            return obj.product_image.first().file.url
        return None
    

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField(method_name='get_category')
    colors = serializers.SerializerMethodField(method_name='get_colors')
    components = serializers.SerializerMethodField(method_name='get_components')
    brand = serializers.SerializerMethodField(method_name='get_brand')
    discount_price = serializers.SerializerMethodField(method_name='get_discount_price')
    images = serializers.SerializerMethodField(method_name='get_images')

    class Meta:
        model = models.Product
        fields = (
            'uuid', 'name', 'price', 'category', 'brand', 'images', 'discount', 'quantity', 'is_top', 'is_common', 'colors', 'components', 'discount_price'
        )

    def get_images(self, obj):
        return [
            {
            "media_product": file_product.file.url
            }
            for file_product in obj.product_image.all()
        ]
    

    
    def get_discount_price(self, obj):
        if obj.discount:
            return obj.price * obj.discount / 100
        
    def get_category(self, obj):
        return {
            'category_id':obj.category.uuid,
            'category_name':obj.category.name
        }
    
    def get_colors(self, obj):
        return [
            {
            'color_name': colors.colour
            }
            for colors in obj.colours.all()
        ]
    
    def get_components(self, obj):
        return[ 
            {
            'info_name':component.info_name,
            'info_text':component.info_text,
            }
            for component in obj.components.all() 
        ]
    
    def get_brand(self, obj):
        return {
            'brand_id':obj.brand.uuid,
            'brand_name':obj.brand.name
        }
    

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryProduct
        fields = (
            'uuid', 'name', 'logo'
        )


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandProduct
        fields = (
            'uuid', 'name',
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery_Form
        fields = (
            'uuid', 'first_name', 'last_name', 'pickup_type', 'region', 'city', 'pickup_address', 'phone_number'
        )


    def create(self, validated_data):
        order = models.Delivery_Form.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            pickup_type = validated_data['pickup_type'],
            region = validated_data['region'],
            city = validated_data['city'],
            pickup_address = validated_data['pickup_address'],
            phone_number = validated_data['phone_number'],
        )

        return {
            'message':"Order created successfullyr"
        }