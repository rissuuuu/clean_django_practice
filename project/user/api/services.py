from user.models import User


def create_user(first_name: str, last_name: str, email: str, password: str,kwargs) -> User:
    user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        **kwargs
    )
    user.set_password(password)
    user.save()
    return user