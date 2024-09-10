from typing import Optional

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

serial_number_validators = [
    RegexValidator(r"^\d{6}$", "Library card number must be exactly 6 digits.")
]


class Rent(models.Model):
    """Model representing a rent of a book."""

    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    rent_date = models.DateTimeField(auto_now_add=True)
    library_card_number = models.PositiveIntegerField(
        validators=serial_number_validators, null=True, blank=True
    )
    return_date = models.DateTimeField(null=True, blank=True)

    def return_book(self) -> None:
        """
        Return the book. Clear the rent_date and library_card_number.
        """
        self.return_date = timezone.now()
        self.save(update_fields=["return_date"])

    def clean(self) -> None:
        """"""
        if self.book.is_rented:
            raise ValidationError("This book is already rented.")
        return super().clean()

    def __str__(self) -> str:
        rent_date = self.rent_date.strftime("%Y-%m-%d %H:%M")
        return_date = (
            self.return_date.strftime("%Y-%m-%d %H:%M") if self.return_date else "###"
        )
        return f"Rent of book {self.book.pk} | {rent_date} - {return_date}"


class Book(models.Model):
    """Model representing a book in the library."""

    serial_number = models.PositiveIntegerField(
        unique=True, primary_key=True, validators=serial_number_validators
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    @property
    def current_rent(self) -> Optional[Rent]:
        """
        Get the current rent of the book. If the book is not rented, return None.
        """
        return self.rent_set.filter(return_date=None).first()

    @property
    def is_rented(self) -> bool:
        """
        Check if the book is rented.
        """
        return self.rent_set.filter(return_date=None).exists()

    def __str__(self) -> str:
        return f"[{self.pk}] {self.title} by {self.author}"
