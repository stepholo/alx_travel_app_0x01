from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from rest_framework import viewsets, permissions, filters


class ListingViewSet(viewsets.ModelViewSet):
    """ViewSet for Listing model"""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'created_at']


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for Booking model"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'listing_title']
    ordering_fields = ['created_at', 'total_price']


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for Review model"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'comment']
    ordering_fields = ['created_at', 'rating']
