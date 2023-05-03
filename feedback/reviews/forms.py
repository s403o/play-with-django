from django import forms


class Reviewform(forms.Form):
    name = forms.CharField(label='Your name', max_length=50, error_messages= {
        'required': 'Please enter your name - must be not empty',
        'max_length': 'Your name is too long'
    })
    review_text = forms.CharField(label='Your feedback', widget=forms.Textarea, max_length=1000, error_messages= {
        'required': 'Please enter your feedback - must be not empty',
        'max_length': 'Your feedback is too long'
    })
    rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5, error_messages= {
        'max_value': 'Please enter a rating between 1 and 5',
        'min_value': 'Please enter a rating between 1 and 5'
    })