from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, MainSection, Section


class MainSectionInlineFormset(BaseInlineFormSet):
    def check_errors(self):
        if self.is_main_counter > 1:
            raise ValidationError('Основным может быть только один раздел.')
        if self.is_main_counter == 0:
            raise ValidationError('Укажите основной раздел')

    def clean(self):
        self.is_main_counter = 0
        for form in self.forms:
            form_data = form.cleaned_data
            if form_data and form_data['is_main']:
                self.is_main_counter += 1
        self.check_errors()
        return super().clean()


class MainSectionInline(admin.TabularInline):
    model = MainSection
    formset = MainSectionInlineFormset
    extra = 1


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [MainSectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['tag_name']