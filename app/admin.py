from django.contrib import admin
from .models import Advertisement, Announcement, Comment


# Advertisement (Reklama) admin
@admin.register(Advertisement)
class AdminAdvertisement(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # bo‘sh joy chiqmasin
    readonly_fields = ("user", "created")  # o‘zgartirib bo‘lmaydi


@admin.register(Announcement)
class AdminAnnouncement(admin.ModelAdmin):
    list_display = (
        "name", "views", "published", "author", "create_at", "update_at", "announcement_image"
    )
    list_filter = ("published", "author")
    search_fields = ("name", "description")
    readonly_fields = ("views", "create_at", "update_at")
    inlines = [CommentInline]  # izohlarni ichida ko‘rsatadi

    def announcement_image(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" width="60px" />')
        return "❌"
    announcement_image.short_description = "Rasm"
