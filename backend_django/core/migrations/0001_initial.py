from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LostFoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('lost', 'Lost'), ('found', 'Found')], max_length=10)),
                ('location', models.CharField(max_length=200)),
                ('image_url', models.URLField(blank=True)),
                ('contact_info', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lostfound_items', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_lostfounditem',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('electronics', 'Electronics'), ('books', 'Books'), ('furniture', 'Furniture'), ('others', 'Others')], max_length=20)),
                ('image_url', models.URLField(blank=True)),
                ('contact_info', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_product',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('preview_text', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('image_url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_items', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_news',
                'ordering': ['-created_at'],
            },
        ),
    ]