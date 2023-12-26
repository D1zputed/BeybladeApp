from django.contrib import admin
from .models import Player, Beyblade, Collection, CurAddress, Mentor

# Register your models here.

@admin.register(Beyblade)
class BeybladeAdmin(admin.ModelAdmin):
    list_display = ("faceBolt", "fusionWheel","spinDirection", "weightGrams", "description", "release_date", "abilities")
    search_fields = ("faceBolt", )
    
@admin.register(CurAddress)
class BeybladeAdmin(admin.ModelAdmin):
    list_display = ("houseNo", "street", "city","province", "country")
    search_fields = ("houseNo", )
    
@admin.register(Mentor)
class BeybladeAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "birthdate","homeTown", "homeCountry", "email")
    search_fields = ("houseNo", )

@admin.register(Player)
class BeybladeAdmin(admin.ModelAdmin):
    list_display = ("mentor", "firstName", "lastName", "birthdate","homeTown", "homeCountry", "email")
    search_fields = ("firstName", )

@admin.register(Collection)
class BeybladeAdmin(admin.ModelAdmin):
    list_display = ("beyblade", "player", "acquisition_date")
    search_fields = ("beyblade", )