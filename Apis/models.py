from django.db import models #type: ignore

class Login(models.Model):
    fullName = models.CharField(max_length=50)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fullName


class Conseil(models.Model):
    class_name = models.CharField(max_length=100)
    description = models.TextField()
    symptoms = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField()
    note = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_name

class Historique(models.Model):
    Login = models.ForeignKey(Login,on_delete=models.CASCADE)
    Conseil = models.ForeignKey(Conseil,on_delete=models.CASCADE)
    prediction_resultat = models.DecimalField(max_digits=5,decimal_places=4)
    date_prediction = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='',null=True,blank=True)
 
    def __str__(self):
        return self.prediction_resultat
    

  