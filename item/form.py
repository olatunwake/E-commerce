from django import forms
from .models import Item


INPUT_CLASSES="w-full py-4 px-6 rounded-xl border"

class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=("name","desc","price","image",'is_sold')
        widget={
            
            "name":forms.TextInput(attrs={
                "class":INPUT_CLASSES
            }),
            "desc":forms.Textarea(attrs={
                "class":INPUT_CLASSES
            }),
        "price":forms.TextInput(attrs={
            "class":INPUT_CLASSES

        }),
        "image":forms.FileInput(attrs={
            "class":INPUT_CLASSES
        })
        }
    
     