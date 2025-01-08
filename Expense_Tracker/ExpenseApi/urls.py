from django.urls import path
from .views import SignUpView, ExpenseListCreate, ExpenseDetail, ExpenseFilterView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
    path('expenses/filter/', ExpenseFilterView.as_view(), name='expense-filter'),
]
