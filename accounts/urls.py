from django.urls import path
from image import views

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
urlpatterns = [
   path('upload/', views.image_upload_view)
  ]