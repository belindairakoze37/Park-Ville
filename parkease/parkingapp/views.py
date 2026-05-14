from django.shortcuts import render,redirect
from .forms import VehicleForm

# Create your views here.
def index(request):
    return render(request,"index.html")


def parking_reg(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehicleForm()
    return render(request, "parking_reg.html", {"form":form})

