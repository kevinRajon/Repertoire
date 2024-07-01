from mesFonctions import (ajouter_contact, supprimer_contact, consulter_contact, nombre_de_contact, trier_contact, rechercher_contact, modifier_contact, travail_termine)

def afficher_menu():
    print("""
    1. Ajouter un contact
    2. Supprimer un contact
    3. Consulter les contacts
    4. Nombre de contacts
    5. Trier les contacts par nom
    6. Rechercher un contact par nom
    7. Modifier un contact par nom
    8. Quitter
    """)

def naviguer_menu():
    while True:
        afficher_menu()
        choix = input("Sélectionnez une option : ")

        if choix == '1':
            nom = input("Nom du contact à ajouter : ")
            prenom = input("Prénom du contact à ajouter : ")
            email = input("Email du contact à ajouter : ")
            ajouter_contact(nom, prenom, email)

        elif choix == '2':
            nom = input("Nom du contact à supprimer : ")
            prenom = input("Prénom du contact à supprimer : ")
            supprimer_contact(nom, prenom)

        elif choix == '3':
            consulter_contact()

        elif choix == '4':
            nombre_de_contact()

        elif choix == '5':
            trier_contact()
            consulter_contact()

        elif choix == '6':
            nom = input("Nom du contact : ")
            rechercher_contact(nom)

        elif choix == '7':
            nom = input("Nom du contact à modifier : ")
            prenom = input("Prénom du contact à modifier : ")
            nouveau_prenom = input("Nouveau prénom : ")
            nouvel_email = input("Nouvel email : ")
            modifier_contact(nom, prenom, nouveau_prenom, nouvel_email)

        elif choix == '8':
            travail_termine()
            break

        else:
            print("Option invalide.")

if __name__ == "__main__":
    naviguer_menu()