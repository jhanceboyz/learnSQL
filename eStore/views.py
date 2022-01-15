
from django.forms import CharField, forms
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Ticket
from django import forms

class Newform(forms.Form):
    searchticket = forms.CharField(label="Search")

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def tickets(request):
        return render(request, 'tickets.html' ,{
            "Tickets": Ticket.objects.all(),
            "Newform": Newform
        })

def searchticket(request):
    if request.method == 'POST':
        print("WORKING ------")
        print(request.POST)
        form = Newform(request.POST)
        if form.is_valid():
            ticketID = form.cleaned_data["searchticket"]
            print(Ticket.objects.get(pk= ticketID))
            print("Finally")
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
