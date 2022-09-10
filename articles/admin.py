from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):

        if len(self.forms) == 0:
            raise ValidationError('Нет тегов!')

        count_main = 0
        for form in self.forms:
            if count_main > 0 and form.cleaned_data.get('id_main'):
                raise ValidationError('Главный тег только один')
            else:
                if form.cleaned_data.get('is_main'):
                    print(f'{form.cleaned_data.get("tag")} --главный раздел')
                    count_main += 1
                else:
                    continue
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


