from django.contrib import admin
from users.models import EmailUser

@admin.register(EmailUser)
class EmailUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscription_level', 'subscription_expires', 'is_active')
