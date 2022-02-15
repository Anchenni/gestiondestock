from django import forms
from .models import Product,Categorie

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('model','categorie','image','status','info')
	
class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ('categorie',)        