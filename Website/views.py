from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response  
from .models import Item, Review, User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from utilities import ardcon1, rdo, read_one
from cart.cart import Cart

# Create your views here.

in_cart= []

class index(generic.ListView):
	template_name = 'Website/index.html'

	def get_queryset(self):
		return Item.objects.all()


def item_details(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'Website/item_details.html', {'item': item})


class register(View):
    form_class = UserForm
    template_name = 'Website/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        already_member = True
        if form.is_valid():
            user = form.save(commit = False)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form, 'already_member': already_member})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        next = request.POST.get('next', '/')

        if user:
            if user.is_active:
                login(request, user)
                return redirect(next)

            else:
                return HttpResponse("Your account is disabled.")
        else:
            if username != "" and password != "":
        	   return render(request, 'Website/login_failed.html', {})
            else:
                return redirect(next)


def add_to_cart(request, pk):
    product = Item.objects.get(pk=pk)
    cart = Cart(request)
    cart.add(product, product.unit_price, 1)

    return redirect('show_cart')
    #return render(request, 'Website/index.html', {})

def remove_from_cart(request, pk):
    product = Item.objects.get(pk=pk)
    cart = Cart(request)
    cart.remove(product)

    return redirect('show_cart')
    #return render(request, 'Website/show_cart.html', {})

def get_cart(request):
    cart = Cart(request)

    pay = 0
    for item in cart:
        pay += int(item.total_price)

    return render(request, 'Website/show_cart.html', {'pay': str(pay), 'cart': Cart(request)})

def thanks_buy(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.quantity -= 1
    item.save()

    #qr_found = ardcon1.func(item.xcord, item.ycord, item.QRcode)
    #if qr_found == item.QRcode:
    #    pass

    return render(request, 'Website/thanks_buy.html', {'item': item})

def thanks_cart(request, cost):
    cart = Cart(request)
    prods = Item.objects.all()

    for item in cart:
        for prod in prods:
            if item.product.name == prod.name:
                pass #call arduino

    #qr_found = ardcon1.func(item.xcord, item.ycord, item.QRcode)
    #if qr_found == item.QRcode:
    #    pass
    return render(request, 'Website/thanks_cart.html', {'cart': cart, 'cost': cost})

def clear_cart(request):
    cart = Cart(request)
    cart.clear()

    return render(request, 'Website/clear_cart.html', {})

def contact_us(request):
    return render(request, 'Website/contact_us.html', {})
