from django.contrib import admin

from .models import Book, Rent


@admin.register(Book)
class BookAdmin(admin.ModelAdmin): ...


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin): ...
