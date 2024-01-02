from typing import Any
from django.shortcuts import render,redirect
from car.models import CarModel,Purchase,Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import CommentForm
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView



from .forms import RegisterForm,LoginForm
# from django.contrib.auth import authenticate, login


class HomeView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = CarModel.objects.all()
        return context
    


    
class Register(View):
    template_name='register.html'
    
    def get(self,request,*args, **kwargs):
        form=RegisterForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args, **kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,self.template_name,{'form':form})
    
class LoginView(View):
    template_name='login.html'
    
    def get(self,request,*args, **kwargs):
        form=LoginForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args, **kwargs):
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,self.template_name,{'form':form})


def car_detail(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)
    comments = Comment.objects.filter(car=car)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=True)
            comment.user = request.user
            comment.car = car
            comment.save()
            
            return redirect('car_detail', car_id=car.id)

    context = {'car': car, 'comments': comments, 'form': form}
    return render(request, 'view_details.html', context)

# class based details post view with comments
class DetailCarView(DetailView):
    model =CarModel
    pk_url_kwarg='car_id'
    template_name='view_details.html'
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        car = self.object #car model er object ekhane store hobe
        comments=car.comments
        if self.request.method == 'POST':
            comment_form =CommentForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment=comment_form.save(commit=False)
                new_comment.car = car
                new_comment.save()
            else:
                comment_form=CommentForm()
            context['comments']=comments
            context['comment_form']=comment_form
            return context
                


# class CarDetails(DetailView):
#     model=CarModel
#     pk_url_kwarg='car_id'
#     template_name='view_details.html'
    
#     def post(self,request,*args, **kwargs):
#         comment_form=CommentForm(data=self.request.POST)
#         car=self.get_object()
#         if comment_form.is_valid():
#              new_comment = comment_form.save()
#              new_comment.post = car
#              new_comment.save()
#              return self.get(request,*args, **kwargs)
    
#     def get_context_data(self, **kwargs) :
#         context=super().get_context_data(**kwargs)
#         car=self.object    
#         comments =car.comments.all()
#         comment_form=CommentForm()
#         context['comments']=comments
#         context['comment_form']=comment_form
#         return context
        

@login_required
def profile(request):
    
    user_purchases = Purchase.objects.filter(user=request.user)

    context = {'user_purchases': user_purchases}
    return render(request, 'profile.html', context)

@login_required
def purchase_car(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)

    if car.quantity > 0:
       
        car.quantity -= 1
        car.save()

        
        Purchase.objects.create(user=request.user, car=car)

        
        return redirect('profile')
   
def add_comment(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.car = car
            comment.save()
            return redirect('car_detail', car_id=car.id)

    return render(request, 'add_comment.html', {'car': car, 'form': form})