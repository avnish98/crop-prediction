from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your username'}))

class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'Type your firstname'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Type your lastname'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Type your email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Type your password again'}))

class ApplicationForm(forms.Form):
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'state', 'placeholder': 'Enter state'}))
    district = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'district', 'placeholder': 'Enter district'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'category', 'placeholder': 'Enter category'}))
    year = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'year', 'placeholder': 'Enter year'}))
    rainfall = forms.FloatField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'rainfall', 'placeholder': 'Enter rainfall'}))
    temp = forms.FloatField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'temp', 'placeholder': 'Enter temp'}))
    area = forms.FloatField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'area', 'placeholder': 'Enter area'}))