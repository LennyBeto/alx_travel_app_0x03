#!/usr/bin/env python3
"""
seed.py

Management command to seed the database with sample listings data.
"""

from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth import get_user_model

User  = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Create sample users
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')

        # Create sample listings
        listing1 = Listing.objects.create(
            title='Cozy Cottage',
            description='A cozy cottage in the countryside.',
            price=100.00,
            location='Countryside',
            owner=user1
        )
        listing2 = Listing.objects.create(
            title='Beach House',
            description='A beautiful beach house with ocean views.',
            price=250.00,
            location='Beachfront',
            owner=user2
        )

        # Create sample bookings
        Booking.objects.create(
            listing=listing1,
            user=user2,
            start_date='2023-01-01',
            end_date='2023-01-07'
        )
        Booking.objects.create(
            listing=listing2,
            user=user1,
            start_date='2023-02-01',
            end_date='2023-02-05'
        )

        # Create sample reviews
        Review.objects.create(
            listing=listing1,
            user=user2,
            rating=5,
            comment='Had a wonderful stay!'
        )
        Review.objects.create(
            listing=listing2,
            user=user1,
            rating=4,
            comment='Great location, but a bit noisy.'
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample data.'))
