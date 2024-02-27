# journaux/models.py
from django.db import models

# class Journal(models.Model):
#     nom = models.CharField(max_length=100)
#     editeur = models.CharField(max_length=42)
#     description = models.TextField(null=True)
#     dateparution = models.DateTimeField(
#         auto_now_add=True, 
#         auto_now=False,
#         verbose_name="Date de parution"
#     )

#     def __str__(self):
#         """
#         Cette méthode que nous définirons dans tous les modèles
#         nous permettra de reconnaître facilement les différents objets que
#         nous traiterons plus tard et dans l'administration
#         """
#         return self.nom
from django.core.validators import MaxValueValidator, MinValueValidator
class Journal(models.Model):
	class Genre(models.TextChoices):
		MANAGEMENT = 'MAN'
		HIGH_TECH = 'IT'
		CUISINE = 'CUI'
		
	nom = models.CharField(max_length=100)
	genre = models.fields.CharField(choices=Genre.choices, max_length=5)
	editeur = models.CharField(max_length=42)
	description = models.TextField(null=True)
	dispo = models.fields.BooleanField(default=True)
	webpage = models.fields.URLField(null=True, blank=True)
	dateparution = models.DateTimeField(
        auto_now_add=True, 
        auto_now=False,
        verbose_name="Date de parution"
    )
    
	year_created = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    
	def __str__(self):
		return self.nom[:50]



class Article(models.Model):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length=42)
	nbpages = models.IntegerField()
	
	# Clé étrangère
	journal = models.ForeignKey(Journal, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.titre[:50]


class Categorie(models.Model):
	nom = models.CharField(max_length=100)
	
	def __str__(self):
		return self.nom[:50]
	
class Livre(models.Model):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length=42)
	date = models.DateTimeField(
        auto_now_add=True, 
        auto_now=False,
        verbose_name="Date de parution"
    )
	
	# Clé étrangère
	categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.titre[:50]
	
