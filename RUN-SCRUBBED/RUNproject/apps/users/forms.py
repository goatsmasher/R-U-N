import floppyforms as forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        widgets = { 'password': forms.PasswordInput()}

class SigninForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
