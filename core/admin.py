from django.contrib import admin
from .models import Pet
from .models import veterinario
from .models import cliente






# Register your models here.

#admin.site.register(PetLost)
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user']

@admin.register(veterinario)
class veterinarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user', 'nome']

@admin.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user', 'nome']




    
