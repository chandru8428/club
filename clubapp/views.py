from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Membership
from .forms import MembershipForm

def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'clubapp/membership_list.html', {'memberships': memberships})

def create_membership(request):
    form = MembershipForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('membership_list')
    return render(request, 'clubapp/create_membership.html', {'form': form})

def update_membership(request, pk):
    membership = get_object_or_404(Membership, pk=pk)
    form = MembershipForm(request.POST or None, instance=membership)
    if form.is_valid():
        form.save()
        return redirect('membership_list')
    return render(request, 'clubapp/update_membership.html', {'form': form})

def delete_membership(request, pk):
    membership = get_object_or_404(Membership, pk=pk)
    if request.method == "POST":
        membership.delete()
        return redirect('membership_list')
    return render(request, 'clubapp/confirm_delete.html', {'membership': membership})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('membership_list')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'clubapp/login.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Membership

@login_required
def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'clubapp/membership_list.html', {'memberships': memberships})


# Create your views here.
