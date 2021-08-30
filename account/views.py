from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.models import Account, SiwesInformation
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, SiwesInfoForm 
# Create your views here.

def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request,'account/home.html', context )

def registration_view(request):
    context ={}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            matric_number = form.cleaned_data.get('matric_number')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(matric_number=matric_number, password=raw_password) 
            login(request, account)
            return redirect ('home')

        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm
        context['registration_form'] = form
    return render(request, 'account/register.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):

    context={}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            matric_number = request.POST['matric_number']
            password = request.POST['password']
            user = authenticate(matric_number=matric_number, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def siwes_info_view(request):# TO edit student siwes information
    if not request.user.is_authenticated:
        return redirect('login') 
    context = {}

    if request.POST:
        form = SiwesInfoForm(request.POST, instance=request.account.siwesinformation)
        if form.is_valid():
            form.save()
            return redirect('home')

       
        
    else:
        form = SiwesInfoForm(instance=request.Account.siwesinformation)

        context['form'] = form
        return render(request, 'account/siwes.html', context)


def account_view(request):#Edits student details
    if not request.user.is_authenticated:
        return redirect('login') 
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AccountUpdateForm(instance=request.user)

    context['form'] = form
    return render(request, 'account/account.html', context)
