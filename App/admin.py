from django.contrib import admin
from .models import *
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)
