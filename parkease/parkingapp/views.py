from django.shortcuts import render,redirect, get_object_or_404
from .forms import VehicleForm
from .models import Vehicle
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def parking_list(request):
    parkings = Vehicle.objects.all()
    return render(request,"parking_list.html", {"parkings":parkings})


@login_required
def parking_reg(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.save()
            vehicle.parking_charge = vehicle.calculate_parking_charge()
            vehicle.save()
            
            return redirect('parking_list')
    else:
        form = VehicleForm()
    return render(request, "parking_reg.html", {"form":form})

@login_required
def edit_parking_reg(request,pk):
    parking = get_object_or_404(Vehicle,pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=parking)
        if form.is_valid():
            form.save()
            return redirect('parking_list')
    else:
        form = VehicleForm(instance=parking)
    return render(request, "parking_reg.html", {"form":form})

@login_required
def delete_parking_reg(request,pk):
    parking = get_object_or_404(Vehicle,pk=pk)
    parking.delete()
    return redirect('parking_list')