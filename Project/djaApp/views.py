from django.shortcuts import render
from django.utils import timezone
from .models import Invoice
#from django.contrib.auth.decorators import login_required, permission_required

#@login_required
#@permission_required('Invoice.can_assign', raise_exception=True)

def invoice_list(request):
    invoices = Invoice.objects.filter(due_date__lte=timezone.now()).order_by('due_date')
    return render(request, 'djaApp/invoice_list.html', {'invoices':invoices})






