from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book, Rent
from .serializers import BookSerializer, RentSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=["post"], url_path=r"rent")
    def rent_book(self, request, pk: int = None) -> Response:
        """Rent the book for provided reader_id. Create a new Rent object."""
        library_card_number = request.data.get("library_card_number")
        if not library_card_number:
            return Response(
                {"error": "library_card_number is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            book = self.get_object()
        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = RentSerializer(
            data={"library_card_number": library_card_number},
            context={"book": book},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(book=book)

        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path=r"return")
    def return_book(self, request, pk: int = None) -> Response:
        """Return the book. It will set the return_date of the current rent."""
        try:
            book = self.get_object()
        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND
            )

        if book.current_rent is None:
            return Response(
                {"error": "The book is not rented."}, status=status.HTTP_400_BAD_REQUEST
            )

        rent: Rent = book.current_rent
        rent.return_book()

        return Response(RentSerializer(rent).data)
