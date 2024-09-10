from rest_framework import serializers

from .models import Book, Rent, serial_number_validators


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class RentSerializer(serializers.ModelSerializer):
    book = BookSerializer(required=False)
    library_card_number = serializers.CharField(validators=serial_number_validators)

    class Meta:
        model = Rent
        fields = "__all__"
        extra_kwargs = {"return_date": {"read_only": True}}

    def validate(self, attrs) -> dict:
        """
        Override the default validate method to check if the book is already rented.
        """
        book = self.context.get("book")
        if book.is_rented:
            raise serializers.ValidationError("This book is already rented.")
        attrs["book"] = book
        return super().validate(attrs)
