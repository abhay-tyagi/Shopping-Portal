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


def index(request):
    items = Item.objects.all()
    rows = 5
    cols = 5

    # xpos = 0
    # ypos = 0

    # with open('positon.txt', 'w') as f:
    #     f.write(str(xpos))
    #     f.write(str(ypos))

    flag = 0
    for item in items:
        if item.xcord == 0:
            flag = 1
            break

    if flag == 1:
        for item in items:
            with open('position.txt', 'r') as f:
                coords = f.read(2)
            xpos = int(coords[0])
            ypos = int(coords[1])

            #movement()

            qr = read_one.funct()
            item.qr = qr
            item.save()


            #print qr

        #go to 0 0

        # with open('positon.txt', 'w') as f:
        #     f.write(str(0))
        #     f.write(str(0))

    return render(request, 'Website/index.html', {'items': items})

def item_details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    reviews = Review.objects.filter(product=item)


    if request.user.is_authenticated:
        new_title = request.GET.get('title')
        new_content = request.GET.get('comment')
        usern = request.user.get_username()

        new_r = Review()
        new_r.title = new_title
        new_r.body = new_content
        new_r.user = User.objects.get(username=usern)
        new_r.product = item

        if new_r.title is not None:
            new_r.save()

    return render(request, 'Website/item_details.html', {'item': item, 'reviews': reviews})


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

def remove_from_cart(request, pk):
    product = Item.objects.get(pk=pk)
    cart = Cart(request)
    cart.remove(product)

    return redirect('show_cart')

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

    # go from 0 0 to item.xcord item.ycord
    # ardcon1.func(item.xcord, item.ycord)
    # if qr_found == item.QRcode:
    #     pass

    return render(request, 'Website/thanks_buy.html', {'item': item})

def thanks_cart(request, cost):
    cart = Cart(request)
    prods = Item.objects.all()

    with open('cartmove.txt', 'w') as f:
        f.write(str(0))
        f.write(str(0))
    
    for item in cart:
        for prod in prods:
            if item.product.name == prod.name:
                # call arduino
                xpos = prod.xcord
                ypos = prod.ycord
                
                with open('positon.txt', 'w') as f:
                    coords = f.read(2)
                xpos = coords[0]
                ypos = coords[1]

                # movement from xpos ypos to item.xcord item.ycord

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
