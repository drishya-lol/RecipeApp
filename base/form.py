from django import forms
from django.contrib.auth.models import User
from .models import Recipe, Category
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid username','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid email address','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user    
        
class LoginForm(forms.Form):  # Change to forms.Form instead of forms.ModelForm
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter a valid username',
        'style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter a password',
        'style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'
    }))

    
class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a category name','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a category description','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
        }
        
class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'process', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a name for the recipe','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the ingredients required to make the recipe','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'process': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How is the recipe made','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select a category','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
        }