from django.urls import path

from product import views


urlpatterns = [
    #product
    path('product-list/', views.ProductListApiView.as_view(), name='product-list'),
    path('detail/<uuid:uuid>/', views.ProductDetailApiView.as_view(), name='product-detail'),
    path('similar/<uuid:uuid>/', views.ProductSimilarListApiView.as_view(), name='product-similar'),
    path('category/', views.ProductCategoryListApiView.as_view(), name='product-category'),
    path('brand/', views.ProductBrandListApiView.as_view(), name='product-brand'),
    path('category-is-common/', views.ProductCategoryIscommonListApiView.as_view(), name='product-category'),
    path('product-new/', views.ProductNewApiView.as_view(), name='product-new'),
    path('product-top/', views.ProductTopApiView.as_view(), name='product-top'),
    path('product-common/', views.ProductCommonApiView.as_view(), name='product-common'),
    path('productby-category/<uuid:uuid>/', views.ProductByCategoryApiView.as_view(), name='productby-category'),
    path('info-nameby-category/<uuid:uuid>/', views.InfoNameByCategoryAPIView.as_view(), name='info-name-category'),
    path('orders-create/', views.OrderCreateApiView.as_view(), name='products-order'),

]