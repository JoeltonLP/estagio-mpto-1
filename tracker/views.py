from helpers import restfy
from .serializers import (
    LegalPersonSerializer,
    StateSerializer, 
    CitySerializer, 
    NaturalPersonSerializer
)


legal_person_index, legal_person_by_id = restfy.make_rest(LegalPersonSerializer)
natual_person_index, natual_person_by_id = restfy.make_rest(NaturalPersonSerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)