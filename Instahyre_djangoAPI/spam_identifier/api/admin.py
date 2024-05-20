from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Contact

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phone_number', 'email'),
        }),
    )
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'user', 'is_spam')
    search_fields = ('name', 'phone_number', 'user__username')

admin.site.register(User, UserAdmin)
admin.site.register(Contact, ContactAdmin)
