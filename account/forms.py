from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
from account.models import SiwesInformation

class RegistrationForm(UserCreationForm):
    email = forms.EmailField( max_length=100, required=True, help_text="Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ('matric_number','full_name','department','college','level','email','password1','password2')


class SiwesInfoForm(forms.ModelForm):
    
    class Meta:
        model = SiwesInformation
        fields = ('bankName', 
             'accountNo',
             'phoneNo',
             'industryName', 
             'industryAddress', 
             'industrySupervisorname',
             'industrySupervisorPhoneno',)






class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = (
            'matric_number',  'full_name', 'email',
            'session', 'college', 'department',
            'gender','level'
            )


class AccountAuthenticationForm(forms.ModelForm): 

    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('matric_number','password')

    def clean(self): #Its an interceptor
        if self.is_valid():
            matric_number = self.cleaned_data['matric_number']
            password = self.cleaned_data['password']
            if not authenticate(matric_number=matric_number, password=password):
                raise forms.ValidationError("Invalid Login")


    
