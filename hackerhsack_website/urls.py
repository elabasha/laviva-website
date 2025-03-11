from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('produkte-sherbime/', views.produkte_sherbime, name="produkte-sherbime"),
    path('blog/', views.blog, name="blog"),
    path('behupartner/', views.behupartner, name="behupartner"),
    path('shop/', views.shop, name="shop"),
    path('kontakt/', views.kontakt, name="kontakt"),
    path('projekte/', views.projekte, name="projekte"),
    path('ndertesa/', views.ndertesa, name="ndertesa"),
    path('sistem_sigurie/', views.sistem_sigurie, name="sistem_sigurie"),  
    path('infrastruktura/', views.infrastruktura, name="infrastruktura"),
    path('sistem_elektrik/', views.sistem_elektrik, name="sistem_elektrik"),
    path('sistem_elektronik/', views.sistem_elektronik, name="sistem_elektronik"),
    path('sistem_energji/', views.sistem_energji, name="sistem_energji"),  
    path('sherbim_website/', views.sherbim_website, name="sherbim_website"),  
    path('sherbime_automatizimi_menaxhimi/', views.sherbime_automatizimi_menaxhimi, name="sherbime_automatizimi_menaxhimi"),
    path('infrastruktura_telekomit/', views.infrastruktura_telekomit, name="infrastruktura_telekomit"),
    path('menaxhim_objekti/', views.menaxhim_objekti, name="menaxhim_objekti"),
    path('qarkullimi_automjeteve/', views.qarkullimi_automjeteve, name="qarkullimi_automjeteve"),
    path('zgjidhje_dixhitale/', views.zgjidhje_dixhitale, name="zgjidhje_dixhitale"),
    path('sisteme_menaxhimit_ndertesave/', views.sisteme_menaxhimit_ndertesave, name="sisteme_menaxhimit_ndertesave"),
    path('sisteme_sigurie/', views.sisteme_sigurie, name="sisteme_sigurie"),  
    path('sisteme_hvac/', views.sisteme_hvac, name="sisteme_hvac"),
    path('sistem_parkimi/', views.sistem_parkimi, name="sistem_parkimi"),
    path('server/', views.server, name="server"),
    path('mekanike/', views.mekanike, name="mekanike"),
    path('air_conditioning/', views.air_conditioning, name="air_conditioning"),
    path('parking_systems/', views.parking_systems, name="parking_systems"),
    path('security_systems/', views.security_systems, name="security_systems"),
]



urlpatterns += [
    path('slide1/', views.slide1, name="slide1"),
    path('slide2/', views.slide2, name="slide2"),
    path('slide3/', views.slide3, name="slide3"),
    path('slide4/', views.slide4, name="slide4"),
    path('slide5/', views.slide5, name="slide5"),
    path('slide6/', views.slide6, name="slide6"),
]


