from dealer.models import Dealer
from user.models import User
from location.models import Province, District
from django.core.exceptions import ObjectDoesNotExist


def create_dealer(
    first_name: str,
    middle_name: str,
    last_name: str,
    province: int,
    district: int,
    latitude: float,
    longitude: float,
    mobile: int,
    email: str,
    user_id: User,
) -> Dealer:
    try:
        province = Province.objects.get(id=province)
    except ObjectDoesNotExist:
        raise ValueError("Province with given id doesnt exist")
    try:
        district = District.objects.get(id=district)
    except ObjectDoesNotExist:
        raise ValueError("District with given id doesnt exist")
    dealer = Dealer.objects.create(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        province=province,
        district=district,
        latitude=latitude,
        longitude=longitude,
        mobile=mobile,
        email=email,
        user_id=user_id,
    )
    return dealer
