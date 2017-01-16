# from django import forms
import floppyforms as forms
from .models import Appointments

class AddForm(forms.ModelForm):
    class Meta:
        model = Appointments
        # fields = '__all__'
        fields = ['date','time','task']
        #
        widgets = {
            'date': forms.TextInput(attrs={'placeholder': '11/07/2017'}),
            'time': forms.DateInput(
                attrs={'placeholder': '18:57'}),
            'task': forms.TimeInput(
                attrs={'placeholder': 'Do it!'}),
        }
        # labels = {
        #     'alias': 'Username',
        # }
        # field_classes = {
        #     # 'email': MySlugFormField,
        # }

class EditForm(forms.ModelForm):
    class Meta:
        model = Appointments
        # fields = '__all__'
        fields = ['task','status','date','time']
        #
        # widgets = { 'password': forms.PasswordInput()}
        #
        # labels = {
        #     'alias': 'Username',
        # }
        # field_classes = {
        #     # 'email': MySlugFormField,
        # }
