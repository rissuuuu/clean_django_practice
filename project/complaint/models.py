from django.db import models
from user.models import User
from dealer.models import Dealer
from orders.models import Orders

class Complaint(models.Model):
    title = models.CharField(max_length=20)
    complain = models.CharField(max_length=100)
    dealer_id = models.ForeignKey(Dealer, blank=True, null=True, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
