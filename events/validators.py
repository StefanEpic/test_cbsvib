from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

POSTCODE_STANDARD = 6


def validate_postcode_field(value: str) -> None:
    """
    Postcode validator.
    """

    if len(value) != POSTCODE_STANDARD:
        raise ValidationError(
            _("The postcode field length must be at 6 numbers"), code="invalid", params={"value": value}
        )

    correct_symbols = r"0123456789"
    for symbol in value:
        if symbol not in correct_symbols:
            raise ValidationError(
                _("The postcode field can only contain numbers"), code="invalid", params={"value": value}
            )
