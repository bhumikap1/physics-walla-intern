from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('image/', views.upload_image, name='upload_file'),  # The upload endpoint
    path('pdf/', views.upload_pdf_file, name='upload_pdf'),
    path('docx/', views.upload_docx_file, name='upload_docx'),
    path('download/', views.download_text, name='download_text'),  # Add this line
]
