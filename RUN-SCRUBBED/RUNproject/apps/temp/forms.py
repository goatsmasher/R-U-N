# from django import forms
import floppyforms as forms
from .models import Event, Invited, Address, Message, Comment
from .google_apis import geocode

# OTHERS = (
#     ('True', 'Allow Others')
# )
# APPROVAL = (
#     ('True', 'Require Approval')
# )

class AddEventForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000, widget=forms.Textarea)
    start_date = forms.CharField(max_length=10)
    start_time = forms.CharField(max_length=10)
    end_date = forms.CharField(max_length=10)
    end_time = forms.CharField(max_length=10)
    # allow_others = forms.CharField( widget=forms.CheckboxSelectMultiple,choices=OTHERS)
    # creater_approve_other_invites = forms.CharField( widget=forms.CheckboxSelectMultiple,choices=APPROVAL)


# class AddForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         # fields = '__all__'
#         fields = ['name','description','']
#         #
#         widgets = {
#             'date': forms.TextInput(attrs={'placeholder': '11/07/2017'}),
#             'time': forms.DateInput(
#                 attrs={'placeholder': '18:57'}),
#             'task': forms.TimeInput(
#                 attrs={'placeholder': 'Do it!'}),
#         }
#         # labels = {
#         #     'alias': 'Username',
#         # }
#         # field_classes = {
#         #     # 'email': MySlugFormField,
#         # }
