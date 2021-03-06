from  django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
# from FYP_ERM.decorators import unauthenticated_user
from django.contrib.auth.forms import UserCreationForm

from dashboard.models import Profile, ProfileSkills
from .forms import CreateUserForms
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponse





# Create your views here.
def logout_views(request):
    if request.method == 'POST':
        logout(request)
        # return redirect('dashboard:dashboard_view')
        return login_view(request)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('dashboard:dashboard_view')
            # return HttpResponse("yes")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/newlogin.html', {'form': form})

def register_view(request):
    form = CreateUserForms()

    if request.method == 'POST':
        form = CreateUserForms(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='client')
            user.groups.add(group)

            messages.info(request, 'Account was Successfully created for ' + username)
            return redirect('accounts:login')

    context = {'form':form}
    return render(request,'accounts/register.html',context)

