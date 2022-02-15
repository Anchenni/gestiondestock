from django.urls import path , include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path("", views.home, name="home"),
path('product/', views.product_list, name='product_list'),
path('product/upload/', views.upload_product, name='upload_product'),
path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),
path('search/', views.search_list, name='search_list'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
