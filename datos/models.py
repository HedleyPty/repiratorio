####
from django.db import models
from datetime import date

class Respiratorio(models.Model):
    nombre= models.CharField(max_length=100, null=False)
    _id=models.CharField(max_length=50, null=False, blank=False)
    instalacion_notifica=models.CharField(max_length=100, null=False)
    tipo_paciente=models.CharField(max_length=1, choices=(("A", "Ambutorio"), ("H", "Hospitalizado")), null=False)
    tipo_identificacion=models.CharField(max_length=1, choices=(("C", "Cédula"), ("P", "Pasaporte"), ("E", "Expediente")), null=False)
    fecha_nacimiento=models.DateField(null=False, default=date.today())
    sexo=models.IntegerField(choices=((1,"Masculino"),(0,"Femenino")),default=1)
    #Geografia
    porta_tarjeta=models.BooleanField(choices=((True, "Sí"),(False, "No")),default=True)
    corresponde_vacuna=models.BooleanField(choices=((True, "Sí"),(False, "No")), default=True)
    Embarazo=models.IntegerField(choices=((1, "Sí"),(0, "No"), (2, "Desconocido"), (3, "No aplica")), default=3)
    hipertension=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    tabaquismo=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    obesidad=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    inmunosupresion=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    alergia=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    otras=models.CharField(max_length=150, null=True)
    riesgo_profesional=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    tipo_riesgo_profesional=models.CharField(max_length=1,
                    choices=(("T", "Trabajador Agropecuario"),("S", "Trabajador de Salud"),("O", "Otro"),
                            ), null=True)
    aislamiento=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    contacto_confirmado=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    tipo_contacto=models.CharField(max_length=1,choices=(("F", "Familiar"),("L", "Laboral"), ("E","Escolar" ), ("O","Otro")), null=True)
    nombre_contacto=models.CharField(max_length=100,null=True)
    viaje_15_dias=models.BooleanField(choices=((True, "Sí"),(False, "No")), null=True)
    Dx_ICD10=models.CharField(max_length=5, null=False, default="JXYZ")
    
    tipo_de_muestra=(("ANF","Aspirado naso faríngeo"),
                    ("BRQ", "Bronquios"),
                    ("HF","Hisopado Faríngeo"),
                    ("HN","Hisopado Nasal"),
                    ("HNF","Hisopado Nasofaringeo"),
                    ("LVA","Lavado Broncoalveolar"),
                    ("LCF","Liquido Cefalorraquideo"),
                    ("LPL", "Liquido Pleural"),
                    ("PLM", "Pulmón"),
                    ("SAN","Sangre"),
                    ("TEJ","Tejido"),
                    ("TRA", "Tráquea"),
    )
    muestra_1_tipo=models.CharField(max_length=3, choices=tipo_de_muestra,
                                    null=False, blank=False)
    muestra_1_toma=models.DateTimeField(auto_now_add=True, null=False)
    muestra_1_envio=models.DateTimeField(auto_now=True, null=True)
    muestra_1_recibido=models.DateTimeField(auto_now=True, null=True)
    muestra_2_tipo=models.CharField(max_length=3, choices=tipo_de_muestra,
                                    null=True, blank=True)
    muestra_2_toma=models.DateTimeField(auto_now_add=True, null=True)
    muestra_2_envio=models.DateTimeField(auto_now=True, null=True)
    muestra_2_recibido=models.DateTimeField(auto_now=True, null=True)
    muestra_3_tipo=models.CharField(max_length=3, choices=tipo_de_muestra,
                                    null=True, blank=True)
    muestra_3_toma=models.DateTimeField(auto_now_add=True, null=True)
    muestra_3_envio=models.DateTimeField(auto_now=True, null=True)
    muestra_3_recibido=models.DateTimeField(auto_now=True, null=True)
    muestra_4_tipo=models.CharField(max_length=3, choices=tipo_de_muestra,
                                    null=True, blank=True)
    muestra_4_toma=models.DateTimeField(auto_now_add=True, null=True)
    muestra_4_envio=models.DateTimeField(auto_now=True, null=True)
    muestra_4_recibido=models.DateTimeField(auto_now=True, null=True)
    muestra_5_tipo=models.CharField(max_length=3, choices=tipo_de_muestra,
                                    null=True, blank=True)
    muestra_5_toma=models.DateTimeField(auto_now_add=True, null=True)
    muestra_5_envio=models.DateTimeField(auto_now=True, null=True)
    muestra_5_recibido=models.DateTimeField(auto_now=True, null=True)