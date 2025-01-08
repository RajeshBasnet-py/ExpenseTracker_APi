from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Expense
from .serializers import UserSerializer, ExpenseSerializer
from datetime import datetime, timedelta

class SignUpView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
   
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseFilterView(APIView):
   
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        filter_type = request.query_params.get('filter')
        today = datetime.today().date()

        if filter_type == 'past_week':
            start_date = today - timedelta(days=7)
        elif filter_type == 'past_month':
            start_date = today - timedelta(days=30)
        elif filter_type == 'last_3_months':
            start_date = today - timedelta(days=90)
        elif filter_type == 'custom':
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            if not start_date or not end_date:
                return Response({"error": "start_date and end_date are required for custom filter"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid filter type"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if filter_type != 'custom':
                expenses = Expense.objects.filter(user=user, date__range=[start_date, today])
            else:
                expenses = Expense.objects.filter(user=user, date__range=[start_date, end_date])
            serializer = ExpenseSerializer(expenses, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
