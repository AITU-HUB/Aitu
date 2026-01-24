import uuid

from django import forms
from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.utils.safestring import mark_safe

from .models import LostFoundItem, Product, News


class LostFoundAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False)

    class Meta:
        model = LostFoundItem
        fields = '__all__'


class ProductAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class NewsAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False)

    class Meta:
        model = News
        fields = '__all__'


@admin.register(LostFoundItem)
class LostFoundAdmin(admin.ModelAdmin):
    form = LostFoundAdminForm
    list_display = ('title', 'status', 'location', 'created_at', 'created_by', 'image_preview')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'location', 'contact_info')
    readonly_fields = ('image_preview', 'created_at')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'status', 'location')}),
        ('Media', {'fields': ('image_url', 'image_file', 'image_preview')}),
        ('Contact', {'fields': ('contact_info',)}),
        ('Meta', {'fields': ('created_at', 'created_by')}),
    )

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" style="max-height: 140px; border-radius: 8px;" />')
        return '—'

    image_preview.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        image_file = form.cleaned_data.get('image_file')
        if image_file:
            storage = FileSystemStorage()
            filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
            obj.image_url = storage.url(filename)
        if not obj.created_by_id:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title', 'category', 'price', 'created_at', 'created_by', 'image_preview')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'contact_info')
    readonly_fields = ('image_preview', 'created_at')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'price', 'category')}),
        ('Media', {'fields': ('image_url', 'image_file', 'image_preview')}),
        ('Contact', {'fields': ('contact_info',)}),
        ('Meta', {'fields': ('created_at', 'created_by')}),
    )

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" style="max-height: 140px; border-radius: 8px;" />')
        return '—'

    image_preview.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        image_file = form.cleaned_data.get('image_file')
        if image_file:
            storage = FileSystemStorage()
            filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
            obj.image_url = storage.url(filename)
        if not obj.created_by_id:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'created_at', 'created_by', 'image_preview')
    list_filter = ('created_at',)
    search_fields = ('title', 'preview_text', 'content')
    readonly_fields = ('image_preview', 'created_at')
    fieldsets = (
        (None, {'fields': ('title', 'preview_text', 'content')}),
        ('Media', {'fields': ('image_url', 'image_file', 'image_preview')}),
        ('Meta', {'fields': ('created_at', 'created_by')}),
    )

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" style="max-height: 140px; border-radius: 8px;" />')
        return '—'

    image_preview.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        image_file = form.cleaned_data.get('image_file')
        if image_file:
            storage = FileSystemStorage()
            filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
            obj.image_url = storage.url(filename)
        if not obj.created_by_id:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)