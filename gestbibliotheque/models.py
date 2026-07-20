from django.db import models

#

class Auteur(models.Model):
    nom =models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    age=models.IntegerField(verbose_name="Veillez saisir votre age ")
    pays=models.CharField(max_length=50,verbose_name="veillez saisir votre pays")

# models pour categorie 

class Categorie(models.Model):
    nom = models.CharField(max_length=50)

# models pour le livre

class Livre(models.Model):
    nom = models.CharField(max_length=50)
    isbn=models.CharField(max_length=10)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_termine =models.DateTimeField(blank=True,null=True)
    
    categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE, related_name='categorie')
    auteur =models.ForeignKey('Auteur',on_delete=models.CASCADE,related_name='auteur')


