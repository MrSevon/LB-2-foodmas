from .models import Orders
from django.forms import ModelForm, TextInput, Textarea

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['bouquet_id', 'name', 'telephone', 'adress', 'comments']

        widgets = {
            "bouquet_id": TextInput(attrs={
                'type': 'text'
            }),
            "telephone": TextInput(attrs={
                'type': 'tel',
                'required pattern': '[0-9]{11}'               
            }),
            "comments": Textarea(attrs={
                'rows': '4'
            })
        }