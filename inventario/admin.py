from django.contrib import admin
from .models import Equipo,EquipoUsuario



class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id','referencia','marca', 'tipo',)
    list_filter = ('tipo',)
    search_fields = ('referencia',)
admin.site.register(Equipo, MyModelAdmin)

class MyModelAdmin2 (admin.ModelAdmin):
    list_display = ('id','key_Equipo','key_user', 'fecha_asig',)
    list_filter = ('fecha_asig','key_user',)

    def PC_elegida(self, obj):

        PC = obj.key_Equipo
        PC.valido = False
        PC.save(update_fields=['valido'])

    
admin.site.register(EquipoUsuario, MyModelAdmin2 )