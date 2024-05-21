from django.urls import path
from .views import LoginView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('docs/', include_docs_urls('Tasks API'))
]