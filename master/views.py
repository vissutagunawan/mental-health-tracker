from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm': '2306214656',
        'name': 'suta',
        'class': 'PBP D',
    }

    return render(request, 'main.html', context)

