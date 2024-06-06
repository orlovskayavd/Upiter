from django.db import models

class Kazakhstan(models.Model):
    Trade_name_rus = models.CharField(max_length=256)
    #Registrator_tran = models.CharField(max_length=256)
    #Registrator_country = models.CharField(max_length=256)
    #Producer_tran = models.CharField(max_length=256)
    #Producer_country = models.CharField(max_length=256)
    #Dosage_form_full_name = models.CharField(max_length=256)
    #Dose = models.CharField(max_length=256)
    #Sc_name = models.CharField(max_length=256)
    #Recipe_status = models.CharField(max_length=256)
    As_name_rus = models.CharField(max_length=256)
    num = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Trade_name_rus
    
    
class Kyrgyzstan(models.Model):
    Trade_name_rus = models.CharField(max_length=256)
    #Registrator_tran = models.CharField(max_length=256)
    #Registrator_country = models.CharField(max_length=256)
    #Producer_tran = models.CharField(max_length=256)
    #Producer_country = models.CharField(max_length=256)
    #Dosage_form_full_name = models.CharField(max_length=256)
    #Dose = models.CharField(max_length=256)
    #Sc_name = models.CharField(max_length=256)
    #Recipe_status = models.CharField(max_length=256)
    As_name_rus = models.CharField(max_length=256)
    num = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Trade_name_rus
    
    
class Armenia(models.Model):
    Trade_name_rus = models.CharField(max_length=256)
    #Registrator_tran = models.CharField(max_length=256)
    #Registrator_country = models.CharField(max_length=256)
    #Producer_tran = models.CharField(max_length=256, default='')
    #Producer_country = models.CharField(max_length=256)
    #Dosage_form_full_name = models.CharField(max_length=256)
    #Dose = models.CharField(max_length=256)
    #Sc_name = models.CharField(max_length=256)
    #Recipe_status = models.CharField(max_length=256)
    As_name_rus = models.CharField(max_length=256)
    num = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Trade_name_rus


class GRLS(models.Model):
    Trade_name_rus = models.CharField(max_length=256)
    #Registrator_tran = models.CharField(max_length=256)
    #Registrator_country = models.CharField(max_length=256) ##############arm krg
    #Producer_tran = models.CharField(max_length=256) ##########grls
    #Producer_country = models.CharField(max_length=256)
    #Dosage_form_full_name = models.CharField(max_length=256)
    #Dose = models.CharField(max_length=256)
    #Sc_name = models.CharField(max_length=256) ###############kz
    #Recipe_status = models.CharField(max_length=256)
    As_name_rus = models.CharField(max_length=256)
    num = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Trade_name_rus
    
    
