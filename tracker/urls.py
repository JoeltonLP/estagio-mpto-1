from django.urls import path
from .views import (
    state_index, 
    state_by_id,
    city_index,
    city_by_id,
    natual_person_index,
    natual_person_by_id
)

urlpatterns = [
    path('natural-person', natual_person_index),
    path('natural-person/<int:id>', natual_person_by_id),
    path('states', state_index),
    path('states/<int:id>', state_by_id),
    path('cities', city_index),
    path('cities/<int:id>', city_by_id),
]
