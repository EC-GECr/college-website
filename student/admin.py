from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'roll_number', 'first_name', 'last_name',
        'email', 'phone', 'enroll_number'
        )

    list_display_links = ('roll_number',)

    search_fields = ('first_name', 'email','roll_number')

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Student, StudentAdmin)
