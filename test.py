def minijeu(x):
    #je def une variable y 
    y = input("devine la lettre")
    #tant que y diff de x 
    while y != x :
        #Alors j'appelerais une nouvelle y 
        y=input("Devine la lettre")
    #lorsque y est égale a x alors
    print("réussi")


#Exercice 1 #Faire une fonction qui concatene 2 chaînes de charactères, les séparants par une virgule  
#DEBUT

str1= "tomato"
str2= "potate"
print(str1, str2, sep=",")

#FIN

#Exercice 2 #Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de charactère #avec l'ensemble des occurences d'un chiffres e.g: #pour tableau = [0,1,1,1,0,1,1,0,1] #la fonction(tableau, 0) doit renvoyer "0,4,7" n'hésitez pas a implémenter la premiere fonction;)  
#Exercice 3 #Renvoyer / Afficher un message
#DEBUT

msg=str(input("Entrez vôtre message : "))
print(msg)

#FIN