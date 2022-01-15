from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Ticket

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def tickets(request):
        return render(request, 'tickets.html' ,{
            "Tickets": Ticket.objects.all()
        })

def searchticket(request, ticketID):
    if request.method == 'POST':
        print("WORKING ------")
        print(ticketID)
    else:
        return render(request, 'tickets.html' ,{
            "Tickets": Ticket.objects.all()
        })

def maketicket(request):
    return render(request, 'maketicket.html')


def ticketdetails(request, ticketID):
    print("WORKING")
    print(ticketID)
    if request.method == 'POST':
        ticketdata = Ticket.objects.get(pk = ticketID)
        print(ticketdata)
        return render(request, 'ticketdetails.html', {
            "ticketdata": ticketdata
        })
