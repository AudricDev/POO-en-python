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

print(user1.nom)
print(user1.getCode())

# instanciation rectangle 
rec1 = Rectangle(100,50)
rec2 = Rectangle(100,50)
rec3 = Rectangle(100,50)


# affichage rectangle 
print(f"Longueur = {rec1.longueur}")
print(f"Largeur = {rec1.largeur}")
