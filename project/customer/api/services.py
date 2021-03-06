from user.models import User
from customer.models import Customer, Commercial, Residential


def register_customer(
    user: User,
    first_name: str,
    middle_name: str,
    last_name: str,
    gender: str,
    mobile: str,
    customer_kind: str,
    picture: str,
) -> Customer:
    customer = Customer.objects.create(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        gender=gender,
        mobile=mobile,
        user_id=user,
        customer_kind=customer_kind,
        picture=picture,
    )
    customer.save()
    return customer


def create_commercial_customer(proprieter_name: str, customer: Customer) -> Commercial:
    commercial = Commercial.objects.create(
        proprieter_name=proprieter_name, customer_id=customer
    )
    commercial.save()


def create_residential_customer(
    customer: Customer, residential_type: str
) -> Residential:
    residential = Residential.objects.create(
        customer_id=customer, kind=residential_type
    )
    residential.save()
