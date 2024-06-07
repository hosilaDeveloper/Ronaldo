from django.contrib import admin
from .models import About, Partner, Resume, AdditionalInfo, Projects
from django.forms import TextInput, Textarea
from django.db import models


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'zip_code')


class AdditionalInfoInline(admin.StackedInline):
    model = AdditionalInfo
    # fields = (('start_finish', 'profession', 'academy'),  'icon', 'content', ('title', 'percent'))
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
    }

    fieldsets = (
        (None, {
            'fields': (('start_finish', 'profession', 'academy'),  ('icon', 'content'))
        }),
        ('Skill info', {
            'fields': (('title', 'percent', 'is_main'), )
        }),
    )
    extra = 0


class ResumeAdmin(admin.ModelAdmin):
    inlines = [AdditionalInfoInline]
    list_display = ('id', 'type', 'is_skill', 'created_at')
    list_filter = ('is_skill', 'created_at')


admin.site.register(About, AboutAdmin)
admin.site.register(Partner)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Projects)
