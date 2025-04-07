
from django.shortcuts import render 
from django.http import JsonResponse
from django.urls import path

def health(request):
    return JsonResponse({"status": "ok"})

def index(request):
    return render(request, 'index.html')
   
def produkte_sherbime(request):
    return render(request, 'produkte-sherbime.html')

def blog(request):
    return render(request, 'blog.html')

def behupartner(request):
    return render(request, 'behupartner.html')

def shop(request):
    return render(request, 'shop.html')  

def kontakt(request):
    return render(request, 'kontakt.html')

def projekte(request):
    return render(request, 'projekte.html')  

def security_systems(request):
    return render(request, 'security_systems.html')

def parking_systems(request):
    return render(request, 'parking_systems.html')

def air_conditioning(request):
    return render(request, 'air_conditioning.html')

def ndertesa(request):
    return render(request, 'ndertesa.html')

def sistem_sigurie(request):
    return render(request, 'sistem_sigurie.html')

def server(request):
    return render(request, 'server.html')

def mekanike(request):
    return render(request, 'mekanike.html')


def infrastruktura(request):
    return render(request, 'infrastruktura.html')

def sherbim_website(request):
    return render(request, 'sherbim_website.html')

def sistem_elektrik(request):
    return render(request, 'sistem_elektrik.html')

def sistem_energji(request):
    return render(request, 'sistem_energji.html')

def sistem_elektronik(request):
    return render(request, 'sistem_elektronik.html')

def menaxhim_objekti(request):
    return render(request, 'menaxhim_objekti.html')

def infrastruktura_telekomit(request):
    return render(request, 'infrastruktura_telekomit.html')

def qarkullimi_automjeteve(request):
    return render(request, 'qarkullimi_automjeteve.html')

def zgjidhje_dixhitale(request):
    return render(request, 'zgjidhje_dixhitale.html')

def sisteme_menaxhimit_ndertesave(request):
    return render(request, 'sisteme_menaxhimit_ndertesave.html')

def sisteme_sigurie(request):
    return render(request, 'sisteme_sigurie.html')

def sisteme_hvac(request):
    return render(request, 'sisteme_hvac.html')

def sistem_parkimi(request):
    return render(request, 'sistem_parkimi.html')


def infrastruktura(request):
    return render(request, 'infrastruktura.html')

def slide1(request):
    return render(request, 'slide1.html')

def slide2(request):
    return render(request, 'slide2.html')

def slide3(request):
    return render(request, 'slide3.html')

def slide4(request):
    return render(request, 'slide4.html')

def slide5(request):
    return render(request, 'slide5.html')

def slide6(request):
    return render(request, 'slide6.html')

def sherbime_automatizimi_menaxhimi(request):
    return render(request, 'sherbime_automatizimi_menaxhimi.html')



# Add more views as needed for other pages
