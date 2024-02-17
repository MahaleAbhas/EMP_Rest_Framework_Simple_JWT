from django.urls import path
from .views import e_api, e_detail_api

urlpatterns = [
    path('run/', e_api),
    path('run/<int:pk>/', e_detail_api)
]
