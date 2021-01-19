from django import forms

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        field = '__all__'