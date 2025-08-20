from django.contrib import admin
from .models import Choice, Question


# Hiển thị Choice trong trang Question
class ChoiceInline(admin.TabularInline):  # Dùng TabularInline cho gọn
    model = Choice
    extra = 3  # Mặc định hiển thị 3 ô trống để thêm Choice mới


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # Gắn ChoiceInline vào QuestionAdmin

    # Các cột hiển thị trong change list
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # Thanh filter bên phải
    list_filter = ["pub_date"]

    # Ô tìm kiếm
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
