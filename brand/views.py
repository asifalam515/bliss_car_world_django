
from django.shortcuts import render, redirect
from django.views import View
from .models import BrandModel
from .forms import AddBrandform

class AddBrandView(View):
    template_name = 'add_brand.html'

    def get(self, request):
        form = AddBrandform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddBrandform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
        return render(request, self.template_name, {'form': form})