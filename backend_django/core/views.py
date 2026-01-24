from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
import uuid

from .forms import LostFoundForm, ProductForm, NewsForm
from .models import LostFoundItem, Product, News


def home(request):
    return render(request, 'core/home.html')


def lostfound_list(request):
    status = request.GET.get('status')
    items = LostFoundItem.objects.all()
    if status in ['lost', 'found']:
        items = items.filter(status=status)
    return render(request, 'core/lostfound_list.html', {'items': items})


def lostfound_detail(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)
    return render(request, 'core/lostfound_detail.html', {'item': item})


@login_required
def lostfound_create(request):
    if request.method == 'POST':
        form = LostFoundForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                storage = FileSystemStorage()
                filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
                item.image_url = storage.url(filename)
            item.created_by = request.user
            item.save()
            return redirect('lostfound_detail', item_id=item.id)
        messages.error(request, 'Please fix the errors in the form.')
    else:
        form = LostFoundForm()
    return render(request, 'core/lostfound_form.html', {'form': form, 'title': 'Create Lost & Found'})


@login_required
def lostfound_edit(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)
    if item.created_by != request.user:
        messages.error(request, 'You can only edit your own listings.')
        return redirect('lostfound_detail', item_id=item.id)
    if request.method == 'POST':
        form = LostFoundForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                storage = FileSystemStorage()
                filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
                item.image_url = storage.url(filename)
            item.save()
            return redirect('lostfound_detail', item_id=item.id)
        messages.error(request, 'Please fix the errors in the form.')
    else:
        form = LostFoundForm(instance=item)
    return render(request, 'core/lostfound_form.html', {'form': form, 'title': 'Edit Lost & Found'})


@login_required
def lostfound_delete(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)
    if item.created_by != request.user:
        messages.error(request, 'You can only delete your own listings.')
        return redirect('lostfound_detail', item_id=item.id)
    if request.method == 'POST':
        item.delete()
        return redirect('lostfound_list')
    return render(request, 'core/confirm_delete.html', {'object': item, 'cancel_url': 'lostfound_detail'})


def product_list(request):
    category = request.GET.get('category')
    items = Product.objects.all()
    if category in ['electronics', 'books', 'furniture', 'others']:
        items = items.filter(category=category)
    return render(request, 'core/product_list.html', {'items': items})


def product_detail(request, item_id):
    item = get_object_or_404(Product, id=item_id)
    return render(request, 'core/product_detail.html', {'item': item})


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                storage = FileSystemStorage()
                filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
                item.image_url = storage.url(filename)
            item.created_by = request.user
            item.save()
            return redirect('product_detail', item_id=item.id)
        messages.error(request, 'Please fix the errors in the form.')
    else:
        form = ProductForm()
    return render(request, 'core/product_form.html', {'form': form, 'title': 'Create Product'})


@login_required
def product_edit(request, item_id):
    item = get_object_or_404(Product, id=item_id)
    if item.created_by != request.user:
        messages.error(request, 'You can only edit your own listings.')
        return redirect('product_detail', item_id=item.id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                storage = FileSystemStorage()
                filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
                item.image_url = storage.url(filename)
            item.save()
            return redirect('product_detail', item_id=item.id)
        messages.error(request, 'Please fix the errors in the form.')
    else:
        form = ProductForm(instance=item)
    return render(request, 'core/product_form.html', {'form': form, 'title': 'Edit Product'})


@login_required
def product_delete(request, item_id):
    item = get_object_or_404(Product, id=item_id)
    if item.created_by != request.user:
        messages.error(request, 'You can only delete your own listings.')
        return redirect('product_detail', item_id=item.id)
    if request.method == 'POST':
        item.delete()
        return redirect('product_list')
    return render(request, 'core/confirm_delete.html', {'object': item, 'cancel_url': 'product_detail'})


def news_list(request):
    items = News.objects.all()
    return render(request, 'core/news_list.html', {'items': items})


def news_detail(request, item_id):
    item = get_object_or_404(News, id=item_id)
    return render(request, 'core/news_detail.html', {'item': item})


def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                storage = FileSystemStorage()
                filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
                item.image_url = storage.url(filename)
            item.created_by = request.user
            item.save()
            return redirect('news_detail', item_id=item.id)
        messages.error(request, 'Please fix the errors in the form.')
    else:
        form = NewsForm()
    return render(request, 'core/news_form.html', {'form': form, 'title': 'Create News'})


@user_passes_test(is_staff)
def news_edit(request, item_id):
    item = get_object_or_404(News, id=item_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                storage = FileSystemStorage()
                filename = storage.save(f'uploads/{uuid.uuid4()}_{image_file.name}', image_file)
                item.image_url = storage.url(filename)
            item.save()
            return redirect('news_detail', item_id=item.id)
        messages.error(request, 'Please fix the errors in the form.')
    else:
        form = NewsForm(instance=item)
    return render(request, 'core/news_form.html', {'form': form, 'title': 'Edit News'})


@user_passes_test(is_staff)
def news_delete(request, item_id):
    item = get_object_or_404(News, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('news_list')
    return render(request, 'core/confirm_delete.html', {'object': item, 'cancel_url': 'news_detail'})