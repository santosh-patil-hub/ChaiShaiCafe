from django.shortcuts import render

# Create your views here.
def HomePage(request):
    """
    Render the home page.
    """
    return render(request, 'App/home.html')