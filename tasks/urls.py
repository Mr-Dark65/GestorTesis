from django.urls import path, include
from .views import FilterOptionsView, LoginView, FacultadViewSet, CarreraViewSet, TutorViewSet, EstudianteViewSet, AvanceViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'facultades', FacultadViewSet)
router.register(r'carreras', CarreraViewSet)
router.register(r'tutores', TutorViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'avances', AvanceViewSet)

urlpatterns = [
    path('api/users/', LoginView.as_view(), name='Users'),
    path('api/filter-options/', FilterOptionsView.as_view(), name='FilterOptions'),
    path('docs/', include_docs_urls('Tasks API')),
    path('', include(router.urls)),
]