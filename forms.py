from django import forms
brand_choice=[
	      ('Select','Select'),	
              ('Honda','Honda'),
              ('Hero','Hero'),
              ('Renault','Renault'),
              ('mahindra','Mahindra'),
       
              ]

class carform(forms.Form):
	
	
	brand=forms.CharField(label= 'Brand name ',widget=forms.Select(choices=brand_choice))
	model=forms.CharField(label= 'model name ',widget=forms.Select(choices=brand_choice))
	
	kilometers=forms.IntegerField(label='kilometers ran')
	power=forms.IntegerField(label='Engine power')
	yeat=forms.IntegerField(label='Year of reg')
	name=forms.CharField(label= 'Enter Your Name')
	email=forms.EmailField(label= 'Enter Email')
	

