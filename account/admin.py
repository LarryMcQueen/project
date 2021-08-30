from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account




class AccountAdmin(UserAdmin):
    ordering = ('full_name',)
    list_display = ('full_name', 'matric_number', 'department', 'level', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('full_name','matric_number', 'department')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

