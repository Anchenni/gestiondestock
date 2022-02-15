from django.db import models
from datetime import datetime
class Categorie(models.Model):
	categorie = models.CharField("Catégorie",max_length=100)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.categorie
	def delete(self, *args, **kwargs):
		super().delete(*args, **kwargs)

class Product(models.Model):
	model = models.CharField("Modèle",max_length=100)
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	# montant = models.DecimalField("Montant",max_digits=10, decimal_places=2)
	date_created = models.DateTimeField(default=datetime.now, blank=True)
	image = models.ImageField("Ajouter une image",upload_to='image/% Y/% m/% d/', blank = True)
	STATUS =(
			('OK', 'OK'),
			('Défectueux', 'Défectueux'))
	status = models.CharField("statut",max_length=200, null=True, choices=STATUS)
	info = models.CharField("Info", max_length=500, blank=True)

	def __str__(self):
		return self.model

	def delete(self, *args, **kwargs):
		self.image.delete()
		super().delete(*args, **kwargs)
