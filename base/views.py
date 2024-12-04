from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm, LoginForm, CreateCategoryForm, CreateRecipeForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Recipe, Category

# Create your views here.
def recipe(request):
    return render(request, 'index.html')

def home(request):
    recipe = Recipe.objects.all()
    return render(request, 'homepage.html', {'recipe': recipe})
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Changed from User to user
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':    
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def createCategory(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listCategory')
        else:
            return render(request, 'createCategory.html', context={'form': form})
    form = CreateCategoryForm()
    data = {'form': form}
    return render(request, "createCategory.html", context = data)

def listCategory(request):
    categories = Category.objects.all()
    return render(request, 'listCategory.html', {'categories': categories})

def editCategory(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('listCategory')
    else:
        form = CreateCategoryForm(instance=category)
    return render(request, 'editCategory.html', {'form': form, 'category': category})

def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('listCategory')

def createRecipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return render(request, 'createRecipe.html', context={'form': form})
    form = CreateRecipeForm()
    data = {'form': form}
    return render(request, "createRecipe.html", context = data)