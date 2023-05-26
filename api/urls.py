from django.urls import path
from .views import all_vehicules, Order_vihicules, vehicules_by_category

urlpatterns = [
    path('vehicules', all_vehicules),
    path('vehicules/category/<str:category>', vehicules_by_category),
    path('vehicules/field/<str:field>/order/<str:order>', Order_vihicules),
    path('vehicules/field/<str:field>/order/<str:order>/category/<str:category>', Order_vihicules)
]
