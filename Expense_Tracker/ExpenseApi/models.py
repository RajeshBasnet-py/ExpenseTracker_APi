from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
   
    CATEGORY_CHOICES = [
        ('Groceries', 'Groceries'),
        ('Leisure', 'Leisure'),
        ('Electronics', 'Electronics'),
        ('Utilities', 'Utilities'),
        ('Clothing', 'Clothing'),
        ('Health', 'Health'),
        ('Others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date = models.DateField()

    class Meta:
        ordering = ['-date']  # Orders by most recent expenses
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __str__(self):
        return f"{self.title} - {self.amount}"
# Compare this snippet from ExpenseApi/admin.py: