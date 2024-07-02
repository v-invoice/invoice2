from django.conf import settings
from django.db import models
from django.utils import timezone
from .static import invoice_status



class Invoice(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_name = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.PositiveSmallIntegerField(choices=invoice_status)
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title