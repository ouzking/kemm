import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()
    

    def la_depense():
        print("Remplissez la liste de vos dépense:")
        le_type = input("donnez le type de depense que voulez-vous ajoutée:\n")
        print(le_type)
        montant = input("donnez le montant de votre dépense:")
        print(montant)
        print("la dépense est ajoutée")
    la_depense()
        
            
    def le_revenu():
        print("Remplissez la liste de vos revenus:")
        son_type = input("donnez le type de revenu que vous voulez ajouté:\n")
        print(son_type)
        montant1 = float(input("donnez le montant de votre revenu:"))
        print(montant1)
        print("le revenu a été consulté")
    le_revenu()
        
    la_depense = []
    le_revenu = []       
    
    def ecart():    
        depense_totale = float(input("réecrivez le solde de votre dépense:"))
        revenu_totale = float(input("réecrivez le solde de votre revenu:"))
        print(depense_totale)
        print(revenu_totale)
        ecart = revenu_totale-depense_totale
        print("l'ecart est:", ecart)
        return ecart
    ecart()
            
    while True:
        choix =""
        print("       Que voulez-vous faire maintenant ?      ")
        print("                                         ")
        print("   C) Révérifier la difference entre la dépense et le revenu")
        print("   0) quitter l'application")
        choix = input("quel est votre désire:\n")
        if choix == "C" or choix == "c":
            print("l'ecart qui existe est de:",la_depense, le_revenu)
            ecart()
        elif choix == "0" or choix == "o" or choix == "O":
            print("Quitter")
            exit()
        else:
            print("votre choix n'est pas reconnu" )