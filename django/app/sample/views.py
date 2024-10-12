from django.http import HttpResponse
import time

# Create your views here.
def index(request):
    time.sleep(1)
    return HttpResponse("Hello, world. You're at the sample index.")