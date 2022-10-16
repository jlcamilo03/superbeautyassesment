from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Equipo(models.Model):
    referencia= models.CharField(max_length=100)
    marca= models.CharField(max_length=100)
    procesador= models.CharField(max_length=100)
    memoria= models.CharField(max_length=100)
    disco= models.CharField(max_length=100)
    TIPO= (
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),)
    tipo=models.CharField(max_length=3, choices=TIPO,default='SSD')
    valido = models.BooleanField(default=True)

    def __str__(self):
        return	self.referencia
    

class EquipoUsuario(models.Model):
	
    key_Equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE,limit_choices_to={'valido':True})  
    key_user=models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asig= models.DateTimeField(default=timezone.now)
    fecha_entr= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return 'equipo N° {} asignado al usuario : {}'.format(self.key_Equipo, self.key_user.username)

    def save(self, *args, **kwargs):
        PC = self.key_Equipo
        elegido = Equipo.objects.get(referencia=PC)
        elegido.valido = False
        elegido.save()
        super(EquipoUsuario, self).save(*args, **kwargs)
 

                