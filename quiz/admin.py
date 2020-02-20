from django.contrib import admin
from quiz.models import Option, Question, Results

class OptionInline(admin.TabularInline):
    model = Option

class QuetsionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

class ResultsAdmin(admin.ModelAdmin):
    list_display = ['name', 'score', 'created_at']

admin.site.register(Results,ResultsAdmin)
admin.site.register(Question,QuetsionAdmin)
