from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm, LoginForm, CreateCategoryForm, CreateRecipeForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Recipe, Category
from django.contrib import messages

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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, 'Invalid username or password')
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

def createRecipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listCategory')
        else:
            return render(request, 'createRecipe.html', context={'form': form})
    form = CreateRecipeForm()
    data = {'form': form}
    return render(request, "createRecipe.html", context = data)

def editRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('listCategory')
    else:
        form = CreateRecipeForm(instance=recipe)
    return render(request, 'editRecipe.html', {'form': form, 'recipe': recipe})

def viewRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'viewRecipe.html', {'recipe': recipe})

def deleteCategory(request, pk):
    if request.method == 'POST':
        category = Category.objects.get(id=pk)
        category.delete()
        messages.success(request, 'Category deleted successfully')
    return redirect('listCategory')

def deleteRecipe(request, pk):
    if request.method == 'POST':
        recipe = Recipe.objects.get(id=pk)
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully')
    return redirect('listCategory') 

def viewCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
        recipes = category.recipe_set.all()  # Assuming the related_name for recipes is `recipe_set`
        return render(request, 'viewCategory.html', {'category': category, 'recipes': recipes})
    except Category.DoesNotExist:
        messages.error(request, "The requested category does not exist.")
        return redirect('listCategory')
