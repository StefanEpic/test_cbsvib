from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

MIN_NAME_LENGTH = 2


def validate_name_field(value: str) -> None:
    """
    Name length and contain letters validator.
    """

    if len(value) < MIN_NAME_LENGTH:
        raise ValidationError(
            _("The name field length must be between 2 and 30 letters"), code="invalid", params={"value": value}
        )

    incorrect_symbols = r"0123456789!\"#$%&'()*+,./:;<=>?@[\]^_{|}~ "
    for symbol in value:
        if symbol in incorrect_symbols:
            raise ValidationError(
                _("The name field can only contain letters or the sign '-'"), code="invalid", params={"value": value}
            )
