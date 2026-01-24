from django import forms
from .models import LostFoundItem, Product, News


class LostFoundForm(forms.ModelForm):
    image_url = forms.CharField(required=False)
    image_file = forms.FileField(required=False)
    class Meta:
        model = LostFoundItem
        fields = ['title', 'description', 'status', 'location', 'image_url', 'contact_info']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Lost student ID card'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the item and details'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Library entrance'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/image.jpg'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'telegram: @username or phone'}),
        }
        help_texts = {
            'image_url': 'Optional. Provide a full URL if available.',
            'image_file': 'Optional. Upload a photo from your device.',
        }


class ProductForm(forms.ModelForm):
    image_url = forms.CharField(required=False)
    image_file = forms.FileField(required=False)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'image_url', 'contact_info']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Used laptop stand'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Condition, size, and notes'}),
            'price': forms.NumberInput(attrs={'min': 0, 'placeholder': 'Price in KZT'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/image.jpg'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'telegram: @username or phone'}),
        }
        help_texts = {
            'image_url': 'Optional. Provide a full URL if available.',
            'image_file': 'Optional. Upload a photo from your device.',
        }


class NewsForm(forms.ModelForm):
    image_url = forms.CharField(required=False)
    image_file = forms.FileField(required=False)
    class Meta:
        model = News
        fields = ['title', 'preview_text', 'content', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'News headline'}),
            'preview_text': forms.TextInput(attrs={'placeholder': 'Short teaser'}),
            'content': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Full news text'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/image.jpg'}),
        }
        help_texts = {
            'image_url': 'Optional. Provide a full URL if available.',
            'image_file': 'Optional. Upload a photo from your device.',
        }
