from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Hey It's me madni in about page")
def contact(request):
    return HttpResponse("Contact Us on 03003079679")