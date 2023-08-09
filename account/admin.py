from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel

# admin.site.register(CustomUserModel, CustomAdmin) # Bu satır yerine aşağıdaki decorator'ı kullandık.
@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Değiştirme Alanı', {
            'fields': ['avatar']
        }),
    )