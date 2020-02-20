from django.contrib import admin
from quiz.models import Option, Question

class OptionInline(admin.TabularInline):
    model = Option

class QuetsionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question,QuetsionAdmin)
