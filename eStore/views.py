from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Ticket,Fault,Customer

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def tickets(request):
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
         i = Customer(name= request.POST['name'],phonenumber= request.POST['phonenumber'],email= request.POST['email'],device= request.POST['device'])
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
        print(ticketdata)
        return render(request, 'ticketdetails.html', {
            "ticketdata": ticketdata
        })
