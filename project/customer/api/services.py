from user.models import User
from customer.models import Customer


def create_user(
    first_name: str, last_name: str, username: str, email: str, password: str
) -> User:
    user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
    )
    user.set_password(password)
    user.save()
    return user


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
