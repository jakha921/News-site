from django.shortcuts import render


def index(request):
    data ={
        'title': 'Главная страница',
        'array': ['Some', 'I am', 'Jakha', '20 yo', 'python developer'],
        'list' : {
            'car': 'Mercedez',
            'age': '20yo',
            'hobby': 'learning',
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
