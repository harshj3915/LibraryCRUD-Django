from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','book_Id','date_added',)

admin.site.register(Book,BookAdmin)


