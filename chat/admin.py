from django.contrib import admin

from .models import Chat, Message


class MessageInlineAdmin(admin.StackedInline):
    model = Message


@admin.register(Chat)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MessageInlineAdmin]
    