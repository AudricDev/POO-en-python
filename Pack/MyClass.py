# declaration

class User():
    # nom = 'RAKOTO'
    # prenom = 'RASOA'
    # age = 12
    # langue = ('FR','MG')
    # coordone = {
    #     'tel':'0330000000',
    #     'Adresse':'Analakely'
    # }

    # Constructeur
    def __init__(self, anarana, fanampiny, fiteny):
        self.nom = anarana
        self.prenom = fanampiny
        self.lang = fiteny

        # propriété prive
        self._code = f'{self.nom}-100'

        # Methode
    def getnom(self):
        return self.nom    

    def getCode(self):
        return self._code
    
    def getLang(self):
        listLang = []
        for e in self.lang:
            affichage = f"{e}"
            listLang.append(affichage)
        return listLang
    # Modifier le nom
    def setNom(self, newname):
        self.nom = newname
    # Supprimer le nom
    def deleteNom(self):
        self.nom = ''
    
    @staticmethod # decorateur : norme universel mihitsy ito rehefa hampiasa methode static, izany hoe tsy mila manpiasa self
    def affichageInfo(x,y):
        print (f"nom : {x} \n prenom : {y}")

# exo 01
class Rectangle():
    def __init__(self,Longueur,largeur):
        self.longueur = Longueur
        self.largeur = largeur
    def surface(self):
        surf = self.longueur * self.largeur
        return surf 
# exo 02
class Player ():
    # methode constructeur
    def __init__(self):
        self.energie = 3
        self.alive = True
    # methode
    def etat_initial(self):
        affichage =  f"Energie initial = {self.energie}"
        return affichage

    def blessure(self):
        self.energie = self.energie - 1
        return self.energie
    def soin(self):
        if self.energie > 0:
            self.energie = self.energie + 1 
            return self.energie
        elif self.energie == 0:
            self.alive = False
            affichage = "impossible de soigner"
            return affichage    
# Heritage
class Function(User):
    def __init__(self, anarana, fanampiny, fiteny, asa):
        super().__init__(anarana, fanampiny, fiteny)
        self.asa = asa
    def getFunction(self):
        return self.asa