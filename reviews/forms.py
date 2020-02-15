from django import forms
from .models import Review

class ReviewCreateForm(forms.ModelForm):
    is_human = forms.BooleanField(label='あなたは人間ですか')

    class Meta:
        model = Review
        exclude = ('created_at',)
        labels = {
            'store_name': 'お店の名前'
        }
        help_texts = {
            'store_name': 'お間違えの無いようにご注意ください'
        }
