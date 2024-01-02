
from django.shortcuts import render, redirect
from django.views import View
from .models import Purchase
from .forms import AddCarForm
from django.contrib.auth.decorators import login_required


# Create your views here.
class AddCarView(View):
    template_name = 'add_car.html'

    def get(self, request):
        form = AddCarForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
        return render(request, self.template_name, {'form': form})
    
