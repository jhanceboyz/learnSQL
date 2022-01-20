from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Ticket,Fault,Customer,Status, Transaction

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def tickets(request):
    if request.method == 'POST':
        i = request.POST['searchticket']
        return render(request, 'tickets.html', {"Tickets": Ticket.objects.filter(id = i)})
    return render(request, 'tickets.html' ,{
            "Tickets": Ticket.objects.all()
        })

def searchticket(request):
    if request.method == 'POST':
        data = request.POST['searchticket']
        return render(request, 'searchticket.html',{
            "data":data
        })

def addcustomer(request):
    if request.method == 'POST':
         i = Customer(name= request.POST['name'],phonenumber= request.POST['phonenumber'],email= request.POST['email'])
         i.save()
         return render(request , 'addcustomer.html',{
            "Tickets": Ticket.objects.all(),
            "Fault": Fault
                })
    else:
        return render(request, 'addcustomer.html',{
            "Tickets": Ticket.objects.all(),
            "Fault": Fault
    })


def ticketdetails(request, ticketID):
    print("WORKING")
    print(ticketID)
    if request.method == 'POST':
        ticketdata = Ticket.objects.get(pk = ticketID)
        return render(request, 'ticketdetails.html', {
            "ticketdata": ticketdata
        })


def maketicket(request):
    if request.method == 'POST':
        print(request.POST.get('customer',False))
        print(request.POST.get('fault_data',False))
        print(request.POST.get('status_data',False))
        print(request.POST.get('amount_data',False))
        print(request.POST.get('device_data',False))
        print(request.POST.get('descriptiondata',False))

        return render(request, 'maketicket.html',{
        "Tickets":Ticket.objects.all(),
        "Fault": Fault.objects.all(),
        "Customer": Customer.objects.all(),
        "Status": Status.objects.all(),
        "Transaction": Transaction.objects.all()
        })
    return render(request, 'maketicket.html',{
        "Tickets":Ticket.objects.all(),
        "Fault": Fault.objects.all(),
        "Customer": Customer.objects.all(),
        "Status": Status.objects.all(),
        "Transaction": Transaction.objects.all()
    })

def searchcustomer(request):
    return render(request, 'searchcustomer.html',{
        "Customer": Customer.objects.all()
    })


def about(request):
    return render(request,'about.html')

def addticket(request):
    if request.method == 'POST':
        print(request.POST['customer'])
        print(Customer.objects.get(pk = request.POST['customer']))
        print(Fault.objects.get(pk = request.POST['fault']))
        print(Status.objects.get(pk = request.POST['status']))
        return render(request, 'addticket.html',{
        "Tickets":Ticket.objects.all(),
        "Fault": Fault.objects.all(),
        "Customer": Customer.objects.all(),
        "Status": Status.objects.all(),
        "Transaction": Transaction.objects.all()
        })

    return render(request, 'addticket.html',{
        "Tickets":Ticket.objects.all(),
        "Fault": Fault.objects.all(),
        "Customer": Customer.objects.all(),
        "Status": Status.objects.all(),
        "Transaction": Transaction.objects.all()
    })