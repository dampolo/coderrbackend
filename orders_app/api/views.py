from rest_framework import viewsets
from orders_app.models import Order
from .serializer import OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from orders_app.permissions import IsOrderAccessAllowed
from django.shortcuts import get_object_or_404
from auth_app.models import Profile

class OrderCreateFromOfferView(viewsets.ModelViewSet):
    permission_classes = [IsOrderAccessAllowed]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(self.get_serializer(order).data, status=status.HTTP_201_CREATED)
    
class OrderCountView(APIView):
    def get(self, request, business_user_id):
        get_object_or_404(Profile, id=business_user_id, type="business")
        count = Order.objects.filter(business_user_id=business_user_id, status="in_progress").count()
        return Response({"order_count": count})
    
class CompletedOrderCountView(APIView):
    def get(self, request, business_user_id):
        get_object_or_404(Profile, id=business_user_id, type="business")
        count = Order.objects.filter(business_user_id=business_user_id, status="completed").count()
        return Response({"completed_order_count": count})