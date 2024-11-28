from django.db import models
from django.core import validators

from common.models import BaseModel

BLACK, RED, WHITE, YELLOW, GREEN, GREY, PINK, BLUE, GOLD, PURPLE, ORANGE = 'black', 'red', 'white', 'yellow', 'green', 'grey', 'pink', 'blue', 'gold', 'purple', 'orange'

class CategoryProduct(BaseModel):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='product/categoty-product/')

    def __str__(self):
        return self.name
    

class BrandProduct(BaseModel):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    

class Product(BaseModel):
    name = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(BrandProduct, on_delete=models.CASCADE, related_name='products')
    discount = models.IntegerField(
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)]
        )
    quantity = models.IntegerField()
    is_top = models.BooleanField(default=False)
    is_common = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductComponents(BaseModel):
    info_name = models.CharField(max_length=120)
    info_text = models.CharField(max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='components')
    

    def __str__(self):
        return self.info_name


class ProductColour(models.Model):
    COLOR_TYPE=(
        (BLACK, BLACK),
        (WHITE, WHITE),
        (RED, RED),
        (GREY, GREY),
        (YELLOW, YELLOW),
        (GREEN, GREEN),
        (BLUE, BLUE),
        (PINK, PINK),
        (GOLD, GOLD),
        (PURPLE, PURPLE),
        (ORANGE, ORANGE),

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colours")
    colour = models.CharField(choices=COLOR_TYPE, max_length=10)

    def __str__(self):
        return f"Product: {self.product.name}|Colour: {self.colour}"
    

class ProductImage(BaseModel):
    file = models.FileField(upload_to='product/product-image/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')

    def __str__(self):
        return self.file.name