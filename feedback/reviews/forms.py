from django import forms


class Reviewform(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)