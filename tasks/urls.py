from django.urls import path
from .views import LoginView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/users/', LoginView.as_view(), name='Users'),
    path('docs/', include_docs_urls('Tasks API'))
]