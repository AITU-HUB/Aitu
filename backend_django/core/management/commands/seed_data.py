from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import LostFoundItem, Product, News


class Command(BaseCommand):
    help = 'Seed initial data for AITU Hub.'

    def handle(self, *args, **options):
        User = get_user_model()

        admin_email = 'admin@aitu.local'
        admin_password = 'admin123'
        if not User.objects.filter(email=admin_email).exists():
            admin_user = User.objects.create_superuser(
                email=admin_email,
                password=admin_password,
                name='AITU Admin',
            )
            self.stdout.write(self.style.SUCCESS(f'Created admin user {admin_email}'))
        else:
            admin_user = User.objects.get(email=admin_email)

        user_email = 'user@aitu.local'
        user_password = 'user123'
        if not User.objects.filter(email=user_email).exists():
            regular_user = User.objects.create_user(
                email=user_email,
                password=user_password,
                name='Student User',
            )
            self.stdout.write(self.style.SUCCESS(f'Created user {user_email}'))
        else:
            regular_user = User.objects.get(email=user_email)

        if not LostFoundItem.objects.exists():
            LostFoundItem.objects.create(
                title='Lost student ID card',
                description='Blue card lost near library entrance.',
                status='lost',
                location='Library entrance',
                image_url='',
                contact_info='telegram: @student_help',
                created_by=regular_user,
            )
            LostFoundItem.objects.create(
                title='Found headphones',
                description='Black wireless headphones found in room 301.',
                status='found',
                location='Room 301',
                image_url='',
                contact_info='telegram: @found_items',
                created_by=regular_user,
            )

        if not Product.objects.exists():
            Product.objects.create(
                title='Used laptop stand',
                description='Aluminum stand, good condition.',
                price=5000,
                category='electronics',
                image_url='',
                contact_info='telegram: @sell_items',
                created_by=regular_user,
            )
            Product.objects.create(
                title='Calculus textbook',
                description='Second edition, minimal notes.',
                price=3000,
                category='books',
                image_url='',
                contact_info='telegram: @books_sell',
                created_by=regular_user,
            )

        if not News.objects.exists():
            News.objects.create(
                title='Welcome to AITU Hub',
                preview_text='The new campus platform is live.',
                content='We are excited to launch AITU Hub for Lost & Found, Buy & Sell, and News.',
                image_url='',
                created_by=admin_user,
            )
            News.objects.create(
                title='Career Fair Next Week',
                preview_text='Meet top employers on campus.',
                content='Join the career fair next week in the main hall. Bring your CV and student ID.',
                image_url='',
                created_by=admin_user,
            )

        self.stdout.write(self.style.SUCCESS('Seed data completed.'))