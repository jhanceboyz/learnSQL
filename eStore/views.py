from os import name
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
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
         return HttpResponseRedirect(reverse('maketicket'))
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
        i = Ticket(customer = Customer.objects.get(pk = request.POST.get('customer',False)),
                    fault = Fault.objects.get(pk =  request.POST.get('fault_data',False)),
                    status = Status.objects.get(pk =  request.POST.get('status_data',False)),
                    description = request.POST.get('descriptiondata',False),
                    device = request.POST.get('device_data',False),
                    transaction = Transaction.objects.get(pk = request.POST.get('amount_data',False)),
                    amount = request.POST.get('amount',False))
        i.save()

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

def addfault(request):
    if request.method == 'POST':
        print(request.POST['fault'])
        i = Fault(name = request.POST['fault'])
        i.save()
        return HttpResponseRedirect(reverse('maketicket'))
    return render(request, 'addfault.html')

def addstatus(request):
    if request.method == 'POST':
        print(request.POST['status'])
        i = Status(name = request.POST['status'])
        i.save()
        return HttpResponseRedirect(reverse('maketicket'))
    return render(request, 'addstatus.html')


def adddata(request):
    Data =Ticket.objects.all()
    result = 0
    for data in Data:
        result = data.amount + result
        print(data.amount)
    print("Total is ", result)
    return render(request, 'about.html')