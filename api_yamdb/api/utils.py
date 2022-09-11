from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from api_yamdb.settings import EMAIL_ADMIN
from reviews.models import User


def send_confirmation_code_to_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = user.confirmation_code
    send_mail(
        'Код подтверждения для завершения регистрации',
        f'Ваш код для получения JWT токена {confirmation_code}',
        EMAIL_ADMIN,
        [user.email],
        fail_silently=False,
    )
