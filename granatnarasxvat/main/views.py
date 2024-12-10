from django.shortcuts import render, redirect
from .models import Bouquets
from .forms import OrdersForm

def home(request):
    return render(request, 'main/home.html')

def bouquets(request):
    bouquets = Bouquets.objects.all()
    return render(request, 'main/bouquets.html', {'bouquets': bouquets})

def delivery(request):
    return render(request, 'main/delivery.html')

def order(request):
    error = ''
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-success')
        else:
            error = 'Форма была не верной'


    form = OrdersForm()
    
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/order.html', data)



def orderSuccess(request):
    return render(request, 'main/order-success.html')