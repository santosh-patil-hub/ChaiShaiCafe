from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    """
    Render the dashboard admin page.
    """
    return render(request, 'Dashboard/dashboard_admin.html')