class CompteBancaire :
    def __init__(self,numeroCompte,nom,solde):
        self.numeroCompte= numeroCompte
        self.nom=nom
        self.solde=solde

    def Versement(self,montantVerse):
        self.solde+=montantVerse

    def Retrait(self,motantRetire):
        if self.solde > motantRetire:
            self.solde -= motantRetire
        print("erreur ,vous n'avez pas cette somme dans votre compte")
    def Agios(self,nbJourDecouvert):
        agio = (self.solde*nbJourDecouvert*0.05)/365
        self.solde -=agio

    def Afficher(self):
        print(f"le compte numero {self.numeroCompte} appartient a {self.nom} et a un solde de {self.solde} FCFA")