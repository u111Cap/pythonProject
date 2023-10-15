import json

print(dir(json))

class CompteBancaire :
    def __init__(self,numeroCompte:int,nom:str,solde:float):
        self.numeroCompte= numeroCompte
        self.nom=nom
        self.solde=solde
        print(self.numeroCompte,self.solde,self.nom)

    def Versement(self,montantVerse:float):
        self.solde+=montantVerse


    def Retrait(self,motantRetire:float):
        if self.solde > motantRetire:
            self.solde -= motantRetire
        else:
            print("erreur ,vous n'avez pas cette somme dans votre compte")


    def Agios(self,nbJourDecouvert:int):
        agio = (self.solde*nbJourDecouvert*0.05)/365
        self.solde -=agio

    def Afficher(self):
        print(f"le compte numero {self.numeroCompte} appartient a {self.nom} et a un solde de {self.solde} FCFA")

cap = CompteBancaire(111,"ivick debertrand",100000)

cap.Versement(500000)
cap.Retrait(250000)
cap.Agios(10)
cap.Afficher()