from django import forms
from .models import Review

# class Reviewform(forms.Form):
#     name = forms.CharField(label='Your name', max_length=50, error_messages= {
#         'required': 'Please enter your name - must be not empty',
#         'max_length': 'Your name is too long'
#     })
#     review_text = forms.CharField(label='Your feedback', widget=forms.Textarea, max_length=1000, error_messages= {
#         'required': 'Please enter your feedback - must be not empty',
#         'max_length': 'Your feedback is too long'
#     })
#     rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5, error_messages= {
#         'max_value': 'Please enter a rating between 1 and 5',
#         'min_value': 'Please enter a rating between 1 and 5'
#     })

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'name': 'Your name',
            'review_text': 'Your feedback',
            'rating': 'Your rating'
        }
        error_messages = {
            'name': {
                'required': 'Please enter your name - must be not empty',
                'max_length': 'Your name is too long'
            },
            'review_text': {
                'required': 'Please enter your feedback - must be not empty',
                'max_length': 'Your feedback is too long'
            },
            'rating': {
                'max_value': 'Please enter a rating between 1 and 5',
                'min_value': 'Please enter a rating between 1 and 5'
            }
        }
        widgets = {
            'review_text': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }