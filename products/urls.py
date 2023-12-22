from rest_framework.routers import DefaultRouter

from products import views

router = DefaultRouter()

router.register(r'products', views.ProductViewSet, 'products')
router.register(r'organizations', views.OrganizationViewSet, 'organizations')
router.register(r'inventories', views.InventoryViewSet, 'inventories')

urlpatterns = router.urls
