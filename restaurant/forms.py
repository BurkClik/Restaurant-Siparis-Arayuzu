from django import forms

class OrderForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField(label="E-Mail")
    phone = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)