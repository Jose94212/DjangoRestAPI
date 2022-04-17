
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=('company_name','shares','avg_price',
            'buy_date','invested_amount','sell_price','sell_date')
        