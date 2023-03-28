from django import forms


class Reviewform(forms.Form):
    name = forms.CharField(label='Your name', max_length=50, error_messages= {
        'required': 'Please enter your name - must be not empty',
        'max_length': 'Your name is too long'
    })