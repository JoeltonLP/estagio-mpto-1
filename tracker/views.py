from helpers import restfy
from .serializers import (
    LegalPersonSerializer,
    PackageContainerSerializer,
    PersonSerializer,
    StateSerializer, 
    CitySerializer, 
    NaturalPersonSerializer
)


(
    package_container_index, 
    package_container_by_id
) = restfy.make_rest(PackageContainerSerializer)
person_index, person_by_id = restfy.make_rest(
    PersonSerializer,
    allow_create=False, 
    allow_update=False, 
    allow_delete=False
)
legal_person_index, legal_person_by_id = restfy.make_rest(LegalPersonSerializer)
natual_person_index, natual_person_by_id = restfy.make_rest(NaturalPersonSerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)