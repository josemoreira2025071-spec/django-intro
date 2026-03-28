from django.contrib import admin

from .models import Choice, Question

import datetime

from django.utils import timezone


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self, obj):  # <-- Add 'obj' here
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= obj.pub_date <= now  # <-- Change 'self' to 'obj' here
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)