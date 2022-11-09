(def input():

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


#Exercice 1 #Faire une fonction qui concatene 2 chaînes de charactères, les séparants par une virgule  
#DEBUT
def concatWithComma(strA, strB):
   #je m'assure que strA soit bien de type str
   stringifiedA = str(strA)
   #je m'assure que strB soit bien de type str
   stringifiedA = str(strB)
   #retourner strA + ',' + strB
   return strA + ',' + strB

concatWithComma(23, "toto"):

#FIN

#Exercice 2 #Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de charactère #avec l'ensemble des occurences d'un chiffres e.g: #pour tableau = [0,1,1,1,0,1,1,0,1] #la fonction(tableau, 0) doit renvoyer "0,4,7" n'hésitez pas a implémenter la premiere fonction;)  
tableau = [0,1,1,1,0,1,1,0,1]
#def la fct findIndex qui itere sur tableau, cherchant l'index des diff occurence de x
def finIndex(tableau, x):
   #def i un index de départ
   i = 0
   #def chaineRetour telle qu'une chaine de caractere vide
   chaineRetour = ''
    #Définir le nombre d'élément du tableau
   #tant que i est diff du nb d'elt dans le tableau
      while (i != lent(tableau)):
         #Alors j'attribue a une variable  la valeur de tableau a l'index i
         selected = tableau[i]
         #  je def un boolen tel que firstTurn est true
         firstTurn = True
         #si selected est égal a x et que firstTurn est true 
         if selected == x and firstTurn == True :
            #Alors on assigne a chainRetour le retour de str(i)
            chainRetour = str(i)
            #changer la valeur de firstTurn a false
            firstTurn = False
         #sinon si selected est egal a x
         if selected == x :
            #alors j'appelle concatWithComma tel que : concatWithComma(chaineRetour, i) à une chaineRetour
            chaineRetour = concatWithComma(chaineRetour, i)
            #j'incremente i de 1
            i = i + 1
#retourne la chaine de retour
return chaineRetour








#definir mon index
i = 0 
while (i != 0 len(tableau)):
   selected = tableau[i]
   i = i + 1









#Exercice 3 #Renvoyer / Afficher un message
#DEBUT

msg=str(input("Entrez vôtre message : "))
print(msg)

#FIN)