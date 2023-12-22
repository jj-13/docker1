from rest_framework.routers import DefaultRouter
from productos.api.viewsets.product_viewsets import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls
