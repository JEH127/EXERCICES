class Voiture:
	voitures_creees = 0
	# constructeur
	def __init__(self, c_name,c_annee):
		### attributs ###
		self.name = c_name   
		self.annee = c_annee
		Voiture.voitures_creees += 1

	    ### méthodes ###
	def modele_voiture(self, c_modele): 
		return c_modele

	def puissance_voiture(self, c_puissance):
		return c_puissance

	def se_deplacer(self):
		print(f"Le véhicule {self.name} se déplace.")
	
v1 = Voiture('Ferrari', 1990)
v2 = Voiture('Porsche', 2000)

print(f" v1 est une {v1.name} de {v1.annee}")
print(f" v1 est un modèle {v1.modele_voiture(250)} de puissance {v1.puissance_voiture(100)} CV ")

print(f" v2 est une {v2.name} de {v2.annee}")
print(f" v2 est un modèle {v1.modele_voiture(500)} de puissance {v2.puissance_voiture(300)} CV ")
print(f" Nombre de voitures crées : {Voiture.voitures_creees}")

v1.se_deplacer()
v2.se_deplacer()