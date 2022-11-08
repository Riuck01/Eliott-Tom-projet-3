
# DEBUT
r = 12000
s = 12500
e = 10
rh = 230
assertionFinal = (((365*3)/(24-(16-8)))*(rh) > r) == (e*s < r)
assertionFinalDeux = (((365*3)/(4-(12-8)))*(rh) > r) == (e*s < r)

partUn = ((365*5)/(24-(16-8)))*(rh) > r  # True
partDeux = e*s < r  # False
part2Un = ((365*5)/(24-(16-8)))*(rh) > r  # False
Part2Deux = (e*s > r) # True

def retournerSixPlusTrois():
   return 6 + 3
   def retournerSixPlusX(x, y):
   return 6 + x

ECRIRE "BJR MONDE"
PRINT ("HELLO WORLD !")
retournerSixPlusTrois()
retournerSixPlusX(9, 4)
print("Quivole un " + retournerSixPlusTrois() + (" Vole un boeuf"))


print ("HELLO WORLD !")
# FIN

#  EXERCICE
# faire def de tt les function
# add(x,y)
# sub(x, y)
# multiply(x, y)
# divide(x, y)
# modulo(x, y)
# SalaireNet(Brut, coeff)
# SalireParSeconde(Salaire horaire, Heure parjourouvr, Nbjoursouvréparan)
#DEBUT
def retournerXPlusY(x,y)
   x+y
def retournerXMoinsY(x,y)
   x-y
def retournerXFoisY(x,y)
   x*y
def retournerXDiviserY(x,y)
   x/y
def retournerXModuloY(x,y)
   x%y
def Snett(Brut, coeff)
 return Brut - Brut*coeff
def salaireParSeconde(salaireHoraire, heureParJourOuvr, NbjoursOuvreParAn)
# calculer mon salaire annuel
   SalaireAnnuel = salaireHoraire * NbjoursOuvreParAn * heureParJourOuvr
   # calculer mon nombre de sencondes en année
   secondeAarAn = 365*24*3600 
   # je pose et je retourne la division
   return SalaireAnnuel/secondeParAn

# Definir une fonction widthFees qui retire un pourcentage a un total en fonction d'un total a un pourcentage
   def widthdrawFees(total, percent)
   #Definir Fees en fonction d'un total et d'un pourcentage
   fees = total * (percent/100)
   #soustraire fees au total
   result = 
   #retourner ma valeur obtenue
#def une fct qui retourne le salaire net en fct du salire brut (float) et du secteur d'activité (ispublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
   #si je suis un travailleur du secteur publique
   if isPublic:
      #Alorsd je soustrais 15% de mon salire brut
      salaireNet = widthdrawFees(salaireBrut, 15)
   #Sinon : Je suis un travailleur du secteur privé
   else:
      #Alors je soustrais 23% de mon salaire brut
      salaireNet = widthdrawFees(salaireBrut, 23)
   #Retourner salaireNet
   return salaireNet

#FIN