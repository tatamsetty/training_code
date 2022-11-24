from django.http import HttpResponse

def app_a(request):
    return HttpResponse("This is APP_a")

def app_b(request):
    return HttpResponse("This is /")
    
def app_home(request):
    return HttpResponse("Welcome to Tinitiate Django app_ti Home Page")