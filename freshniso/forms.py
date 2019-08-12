from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or Suite'
    }))
    country = CountryField(blank_label='(select a country)').formfield(attrs={
        'class': 'custom-select d-block w-100'
    })
    zip = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input'
    }))
    save_info = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input'
    }))
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'placeholder': '1234 Main St'
    }), choices=PAYMENT_CHOICES)
