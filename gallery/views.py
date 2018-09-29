from django.shortcuts import render,redirect
from .models import Image,Location,Category
# Create your views here.
def Gallery(request):
    personal = Image.display_image('personal')
    travel = Image.display_image('travel')
    sports = Image.display_image('sports')
    family= Image.display_image('family')
    return render(request, 'index.html',{"personal":personal,"travel":travel,"sports":sports,"family":family})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'searched.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searched.html',{"message":message})  