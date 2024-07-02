from django.shortcuts import render
from django.utils import timezone
from .models import Invoice

def invoice_list(request):
    invoices = Invoice.objects.filter(due_date__lte=timezone.now()).order_by('due_date')
    return render(request, 'djaApp/invoice_list.html', {})


