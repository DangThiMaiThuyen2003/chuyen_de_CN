from rest_framework import routers
from apiApp.views.role_views import RoleViewSet, PermissionViewSet

router = routers.DefaultRouter()
router.register(r'', RoleViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = router.urls