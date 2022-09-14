import datetime

from django.core.exceptions import ValidationError


def validator_pub_year(value):
    if value < 1308 or value > datetime.datetime.now().year:
        raise ValidationError(f'{value} — is not a correct year!')
