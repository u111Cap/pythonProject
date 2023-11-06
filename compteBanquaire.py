#retrait de l'import json 

class CompteBancaire :
    def __init__(self,numeroCompte:int,nom:str,solde:float):
        self.numeroCompte= numeroCompte
        self.nom=nom
        self.solde=solde
        print(self.numeroCompte,self.solde,self.nom)

    def Versement(self):
        #ajout d'une boucle pour gerer les entrées du User
        test=True
        while test:    
            try:
                
                montantVerse=float(input("Entrer le montant de votre versement: \n"))

                 #controle sur le montant à verser les valeurs negatives  et caractères non admis
                if montantVerse>=0:
                    self.solde+=montantVerse
                    print(f"Versement de {montantVerse} effectué. Nouveau solde : {self.solde}")
                    break
                elif montantVerse<0: 
                    print("Le Montant  Entré Est Invalide")
                    continue
            except:
                print("Valeur Invalide.Saisissez un montant en chiffre") 
               


    def Retrait(self):
         #ajout d'une boucle pour gerer les entrées du User
        test=True
        while test: 
                try:
                    motantRetire=float(input("Entrer le montant de votre retrait: \n"))
                    # controle des valeurs negatives
                    if motantRetire <0 :
                        print("Valeur non reconnue.Veuillez entrer un numerique non négatif")
                        continue
                    elif self.solde > motantRetire:
                        self.solde -= motantRetire
                        print(f"Retrait de {motantRetire} effectué. Nouveau solde : {self.solde}")
                        break
                    else:
                        print("erreur ,vous n'avez pas cette somme dans votre compte")
                except:
                    print("Valeur Invalide.Saisissez un montant en chiffre")    

     # Pourquoi le calcul du Agios n'est pas le même dans tous les projets
    def Agios(self,nbJourDecouvert:int):
       
        agio = (self.solde*nbJourDecouvert*0.05)/365
        self.solde -=agio
    

    def Afficher(self):
        print(f"le compte numero {self.numeroCompte} appartient a {self.nom} avec un solde de {self.solde} FCFA")

cap = CompteBancaire(111,"ivick debertrand",0)
#permettre à l'utlisateur d'interagir avec le programme
cap.Versement()
cap.Retrait()
cap.Agios(10)
cap.Afficher() 
