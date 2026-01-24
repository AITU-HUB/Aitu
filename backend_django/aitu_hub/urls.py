from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views
from core import views as core_views
from accounts.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('register/', account_views.register, name='register'),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),

    path('lostfound/', core_views.lostfound_list, name='lostfound_list'),
    path('lostfound/<int:item_id>/', core_views.lostfound_detail, name='lostfound_detail'),
    path('lostfound/create/', core_views.lostfound_create, name='lostfound_create'),
    path('lostfound/<int:item_id>/edit/', core_views.lostfound_edit, name='lostfound_edit'),
    path('lostfound/<int:item_id>/delete/', core_views.lostfound_delete, name='lostfound_delete'),

    path('products/', core_views.product_list, name='product_list'),
    path('products/<int:item_id>/', core_views.product_detail, name='product_detail'),
    path('products/create/', core_views.product_create, name='product_create'),
    path('products/<int:item_id>/edit/', core_views.product_edit, name='product_edit'),
    path('products/<int:item_id>/delete/', core_views.product_delete, name='product_delete'),

    path('news/', core_views.news_list, name='news_list'),
    path('news/<int:item_id>/', core_views.news_detail, name='news_detail'),
    path('news/create/', core_views.news_create, name='news_create'),
    path('news/<int:item_id>/edit/', core_views.news_edit, name='news_edit'),
    path('news/<int:item_id>/delete/', core_views.news_delete, name='news_delete'),

    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)