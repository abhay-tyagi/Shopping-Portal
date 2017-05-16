from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Item, Review, User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View

# Create your views here.

class index(generic.ListView):
	template_name = 'Website/index.html'

	def get_queryset(self):
		return Item.objects.all()


def item_details(request, pk):
    item = get_object_or_404(Item, pk=pk)

    lst = []
    for i in range(item.quantity):
        lst.append(i+1)
    qty = ''.join(str(e) for e in lst)
    print(qty)

    return render(request, 'Website/item_details.html', {'item': item, 'qty': str(qty)})


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
        	return render(request, 'Website/login_failed.html', {})

def thanks(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.quantity -= 1
    item.save()
    return render(request, 'Website/thanks.html', {'item': item})

def contact_us(request):
    return render(request, 'Website/contact_us.html', {})
