from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'create.html')

def show(request, id):
    print(id)
    # buscar un muro
    return render(request, 'create.html')

def edit(request, id):
    print(id)
    # buscar un muro
    return render(request, 'create.html')
    