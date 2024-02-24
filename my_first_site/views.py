from django.http import  HttpResponse

def print_hello(request):
    return HttpResponse('<p>hellooo</p>')
def print_arhiv(request):
    return HttpResponse('<p>Arhiiiiiiiv</p>')