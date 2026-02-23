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
class Rectangle():
    def __init__(self,Longueur,largeur):
        self.longueur = Longueur
        self.largeur = largeur