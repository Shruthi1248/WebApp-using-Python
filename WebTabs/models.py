from django.db import models

class FormData(models.Model):
    form_key = models.CharField(max_length=100,default="empty")
    forms_name= models.CharField(max_length=255,default="value")
    Rediretpath_name = models.CharField(max_length=100,default="value")
    
    
    def str(self):
        return f"{self.forms_name} " 
    
class FieldData(models.Model):
    field_key = models.CharField(max_length=100,default="empty")
    field_value= models.CharField(max_length=255,default="value")
    selection_value = models.CharField(max_length=100,default="value")
    required=models.BooleanField(default=None,null=True)
    readable=models.BooleanField(default=None,null=True)
    
    def str(self):
        return f"{self.field_key}"
    
class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)