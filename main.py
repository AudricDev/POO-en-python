from Pack.MyClass import User
from Pack.MyClass import Rectangle

#instance
# user1 = User()
# print(user1.nom)
# print(user1.coordone["tel"])
# print(user1.coordone["Adresse"])

user1 = User("RABE","Kely",['FR','MG'])
user2 = User("RASON","Kely",['MG','EN'])
user3 = User("RAVELO","kely",['FR','MG'])


print(f"Nom taloha : {user1.nom}")
print(user1.getCode())
print(f"Liste langage : {user1.getLang()}")
print(f"Valeur 1er langage : {user1.getLang()[0]}")
print(f"Valeur 2eme langage : {user1.getLang()[1]}")

user1.setNom("Audre")
print(f"Nom vaovao modifier par setNom = {user1.nom}")

user1.deleteNom()
print(f"Nom supprimer apres setNom = {user1.nom}")

# utilisation methode static
print(user1.affichageInfo(user1.nom,user1.prenom))

# instanciation rectangle 
rec1 = Rectangle(100,50)
rec2 = Rectangle(200,100)
rec3 = Rectangle(300,200)

# affichage rectangle 
print(f"Longueur = {rec1.longueur}")
print(f"Largeur = {rec1.largeur}")

# surface rectangle
print(f"Surface Rectangle 1 = {rec1.surface()}")
print(f"Surface Rectangle 2 = {rec2.surface()}")
print(f"Surface Rectangle 3 = {rec3.surface()}")

