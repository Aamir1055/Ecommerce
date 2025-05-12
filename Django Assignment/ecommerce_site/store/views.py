from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, OrderItem
from .serializers import *
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['price']
    search_fields = ['name']

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_seller:
            raise PermissionDenied("Only sellers can add products.")
        serializer.save(seller=self.request.user)
    

    def perform_create(self, serializer):
        if not self.request.user.is_seller:
            raise PermissionError("Only sellers can add products.")
        serializer.save(seller=self.request.user)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_buyer:
            return Order.objects.filter(buyer=user)
        elif user.is_seller:
            return Order.objects.filter(orderitem__product__seller=user).distinct()
        return Order.objects.none()

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_buyer:
            raise PermissionError("Only buyers can create orders.")
        serializer.save(buyer=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

