from rest_framework.routers import DefaultRouter
from persona_app.api.viewsets.persona_viewsets import PersonaViewSet

router = DefaultRouter()
router.register(r'persona', PersonaViewSet, basename='persona')

urlpatterns = router.urls
