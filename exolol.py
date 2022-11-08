def input():

#renvoie un caractere de type string au hasard

#Exercice:
   #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractere
      #definir le caractere a trouver
      caractere = str(input("Definisse le caractere a trouver"))
      #Compteur 
      compteur = 1
      #creer une boucle repeté tant que le caractere ne correspond pas
      while input() != str(input("Definisse le caractere a trouver")):
         #compteur
         compteur = compteur + 1
         #si le caractere correspond
      else : 
         print("ta gagné bg"+ str(compteur) + "essaie")
      #Afficher "gagné"

   #le caractere doit être parametrable


#FIN

#CORRECTION 
#je def un mini jeu 
def minijeu(x):
    #je def une variable y 
    y = input("devine la lettre")
    #tant que y diff de x 
    while y != x :
        #ajouter un compteur
        compteur = compteur + 1
        #afficher le compteur
        print(compteur)
        #Alors j'appelerais une nouvelle y 
        y=input("Devine la lettre")
    #lorsque y est égale a x alors
    print("réussi")


prenom = "Tom"
nom = "Forest"
identite = nom + prenom # retourne "ForestTom"

identite = nom + '' + prenom # retourne "Forest Tom"

integerValue = 342 #retourne 342
stringIntegerValue = str(342)
mlg = [1,2,3,4,87,3,6,45,2]