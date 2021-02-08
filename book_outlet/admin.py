from django.contrib import admin

# Register your models here.
from book_outlet.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "rating", "author", "is_bestselling")


admin.site.register(Book, BookAdmin)
