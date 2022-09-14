from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from api_yamdb.settings import EMAIL_ADMIN
from reviews.models import Title, User


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


class CurrentTitleDefault:
    requires_context = True

    def __call__(self, serializer_field):
        title_id = serializer_field.context['view'].kwargs.get('title_id')
        return get_object_or_404(Title, id=title_id)

    def __repr__(self):
        return '%s()' % self.__class__.__name__
