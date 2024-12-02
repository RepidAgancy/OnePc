from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

BLACK, RED, WHITE, YELLOW, GREEN, GREY, PINK, BLUE, GOLD, PURPLE, ORANGE = _('black'), _('red'), _('white'), _('yellow'), _('green'), _('grey'), _('pink'), _('blue'), _('gold'), _('purple'), _('orange')
DELIVERY, TAKEFROM_HERE = _('delivery'), _('takefrom_here')

class CategoryProduct(BaseModel):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='product/categoty-product/')
    is_common = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Mahsulotlar Kategoriyasi")
        verbose_name_plural = _("Mahsulotlar Kategoriyasi")
    

class BrandProduct(BaseModel):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Mahsulotning Brandi")
        verbose_name = _("Mahsulotlarning Brandi")

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
    
    class Meta:
        verbose_name = _("Mahsulot")
        verbose_name = _("Mahsulotlar")


class ProductComponents(BaseModel):
    info_name = models.CharField(max_length=120)
    info_text = models.CharField(max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='components')
    

    def __str__(self):
        return self.info_name
    
    class Meta:
        verbose_name = _("Mahsulot xususiyat")
        verbose_name_plural = _("Mahsulot xususiyatlari")


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
    
    class Meta:
        verbose_name = _("Mahsulot rang")
        verbose_name_plural = _("Mahsulot ranglari")
    

class ProductImage(BaseModel):
    file = models.FileField(upload_to='product/product-image/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name = _("Mahsulot rasm")
        verbose_name_plural = _("Mahsulot rasmlari")


class Delivery_Form(BaseModel):
    TYPE=(
        (DELIVERY, DELIVERY),
        (TAKEFROM_HERE, TAKEFROM_HERE)
    )
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    pickup_type = models.CharField(max_length=120, choices=TYPE)
    region = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    pickup_address = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class OrderProduct(BaseModel):
    delivery_from = models.ForeignKey(Delivery_Form, on_delete=models.CASCADE, related_name='orders')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.delivery_from} {self.products}"
    
    class Meta:
        verbose_name = _("Buyurtmadagi mahsulot")
        verbose_name_plural = _("Buyurtmadagi mahsulotlar")