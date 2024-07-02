from tabulate import tabulate
complete=False
while complete==False:
    ID = str(input('ID '))
    name = str(input('Customer Name '))
    amount = float(input('Amount '))
    dueDate=str(input('Due date'))
    status=('Pending')#approved/rejected/on-hold(default=pending)
    #row=[ID, name, amount, dueDate, status]
    dataInvoices = {'Invoice ID': ID,'Customer name': name, 'Amount': amount, 'Due date': dueDate, 'Status': status} #dictionary
    #dataInvoices.append(row)   
    header=['ID','Name', 'Amount', 'Due Date', 'Status']
    #print(tabulate(dataInvoices, headers=header, tablefmt="grid"))
    print(dataInvoices)
    finish = str(input('Complete?'))
    if finish=='yes':
        complete=True

