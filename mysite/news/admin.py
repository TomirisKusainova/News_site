from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import News, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'created_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields=('title', 'category', 'content', 'is_published', 'created_at') # поля которые хотим увидеть и изменять
    readonly_fields = ('is_published', 'created_at') # те поля которые нельзя редактировать только для просмотра

    # def get_photo(self, obj):
    #     if obj.photo:
    #          return mark_safe(f'<img scr="{obj.photo.urls}" width="75">')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
