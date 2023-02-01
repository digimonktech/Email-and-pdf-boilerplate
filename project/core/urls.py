from django.urls import path, include
from .views import EmailView, PDFView

urlpatterns = [
    path("email/", EmailView.as_view(), name="email"),
    path("pdf/", PDFView.as_view(), name="pdf"),
]
