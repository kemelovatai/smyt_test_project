from rest_framework.routers import DefaultRouter

from orders import views

router = DefaultRouter()

router.register(r'orders', views.OrderViewSet, 'orders')

urlpatterns = router.urls
