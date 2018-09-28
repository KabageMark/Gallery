from django.shortcuts import render,redirect
from .models import Image,Location,Category
# Create your views here.
def Gallery(request):
    image = Image.display_image()
    return render(request, 'index.html',{"image":image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        result_images = f"{search_term}"

        return render(request, 'searched.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searched.html',{"message":message})  