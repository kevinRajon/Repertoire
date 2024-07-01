def ajouter_contact(nom, prenom, email, fichier="contacts.txt"):
    try:
        # Ouvre le fichier en mode append ('a') pour ajouter à la fin
        with open(fichier, 'a') as file:
            # Écrit une nouvelle ligne avec les informations du contact
            file.write(f"{nom},{prenom},{email}\n")
        # Affiche un message de confirmation
        print(f"Contact {prenom} {nom} ajouté.")
    except Exception as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"Erreur lors de l'ajout du contact : {e}")

def consulter_contact(fichier="contacts.txt"):
    try:
        # Ouvre le fichier en mode lecture ('r')
        with open(fichier, 'r') as file:
            # ajoute toutes les lignes à la variable (lignes) dans une liste
            lignes = file.readlines()
        
        if lignes:
            # affiche tous les contacts
            print("Liste des contacts :")
            for ligne in lignes:
                # Découpe chaque ligne en nom, prénom, email et affiche les détails
                nom, prenom, email = ligne.strip().split(',')
                print(f"Nom: {nom}, Prénom: {prenom}, Email: {email}")
        else:
            # Si aucune ligne n'est trouvée
            print("Aucun contact trouvé.")
    except Exception as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"Erreur lors de la consultation des contacts : {e}")

def modifier_contact(nom, prenom, nouveau_prenom, nouvel_email, fichier="contacts.txt"):
    try:
        # Ouvre le fichier en mode lecture ('r') 
        with open(fichier, 'r') as file:
            lignes = file.readlines()

        contact_modifie = False # declare une vazriable pour verifier si le copntact est modifié
        # Ouvre le fichier en mode écriture ('w')
        with open(fichier, 'w') as file:
            for ligne in lignes:
                # Découpe chaque ligne en nom, prénom, email
                nom_ligne, prenom_ligne, email_ligne = ligne.strip().split(',')
                # Vérifie si le contact correspond à celui à modifier
                if nom_ligne.lower() == nom.lower() and prenom_ligne.lower() == prenom.lower():
                    # Écrit le contact avec les nouvelles informations
                    file.write(f"{nom},{nouveau_prenom},{nouvel_email}\n")
                    contact_modifie = True
                else:
                    # Réécrit les lignes inchangées pour les autres contacts
                    file.write(ligne)

        if contact_modifie:
            # Affiche un message si le contact a été modifié
            print(f"Contact {prenom} {nom} modifié.")
        else:
            # Affiche un message si le contact n'a pasd été trouvé
            print(f"Aucun contact trouvé avec le nom {nom} et le prénom {prenom}.")
    except Exception as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"Erreur lors de la modification du contact : {e}")

def nombre_de_contact(fichier="contacts.txt"):
    try:
        # Ouvre le fichier en mode lecture ('r')
        with open(fichier, 'r') as file:
            # Lit toutes les lignes
            lignes = file.readlines()
        
        # Calcule le nombre lignes
        nombre_contacts = len(lignes)
        # Affiche le nombre de contacts
        print(f"Nombre de contacts : {nombre_contacts}")
        return nombre_contacts
    except Exception as e:
        # affiche un message d'erreur
        print(f"Erreur lors du comptage des contacts : {e}")
        return 0

def rechercher_contact(nom, fichier="contacts.txt"):
    try:
        # Ouvre le fichier en mode lecture ('r')
        with open(fichier, 'r') as file:
            # Lit toutes les lignes
            lignes = file.readlines()
        
        contacts_trouves = []
        # Parcourt chaque ligne pour rechercher le nom 
        for ligne in lignes:
            nom_ligne, prenom_ligne, email_ligne = ligne.strip().split(',')
            if nom_ligne.lower() == nom.lower():
                # Ajoute les contacts trouvés à la liste
                contacts_trouves.append((nom_ligne, prenom_ligne, email_ligne))
        
        if contacts_trouves:
            # Affiche les contacts trouvés avec le nom 
            print(f"Contact trouvé avec le nom {nom} :")
            for contact in contacts_trouves:
                print(f"Nom: {contact[0]}, Prénom: {contact[1]}, Email: {contact[2]}")
        else:
            # Affiche un message si aucun contact n'est trouvé
            print(f"Aucun contact trouvé avec le nom {nom}.")
    except Exception as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"Erreur lors de la recherche du contact : {e}")

def supprimer_contact(nom, prenom, fichier="contacts.txt"):
    try:
        # Ouvre le fichier en mode lecture ('r')
        with open(fichier, 'r') as file:
            # Lit toutes les lignes
            lignes = file.readlines()

        contact_supprime = False # declare une variable pour verifier si contatc suppr
        # Ouvre le fichier en mode écriture ('w') 
        with open(fichier, 'w') as file:
            for ligne in lignes:
                # Découpe chaques lignes en nom, prénom, email
                nom_ligne, prenom_ligne, email_ligne = ligne.strip().split(',')
                # Vérifie si le contact correspond à celui à supprimer
                if nom_ligne.lower() != nom.lower() or prenom_ligne.lower() != prenom.lower():
                    # Réécrit les lignes inchangées pour les autres contacts
                    file.write(ligne)
                else:
                    # Indique que le contact a été trouvé et supprimé
                    contact_supprime = True

        if contact_supprime:
            # Affiche un message si le contact a été suppriméf
            print(f"Contact {prenom} {nom} supprimé .")
        else:
            # Affiche un message si aucun contact n'a été trouvé
            print(f"Aucun contact trouvé.")
    except Exception as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"Erreur lors de la suppression du contact : {e}")

def trier_contact(fichier="contacts.txt"):
    try:
        # Ouvre le fichier en mode lecture ('r')
        with open(fichier, 'r') as file:
            # Lit toutes les lignes
            lignes = file.readlines()
        
        if lignes:
            # Trie les contacts par ordre alphabétique du nom
            contacts = [ligne.strip().split(',') for ligne in lignes]
            contacts_triees = sorted(contacts, key=lambda contact: contact[0].lower())

            # Ouvre le fichier en mode écriture ('w') pour écraser les données existantes
            with open(fichier, 'w') as file:
                for contact in contacts_triees:
                    # Réécrit les lignes triées dans le fichier
                    file.write(','.join(contact) + '\n')
            
            # Affiche un message si les contacts ont été triés avec succès
            print("Contacts triés par ordre alphabétique de nom.")
        else:
            # Affiche un message si aucun contact n'est présent pour le tri
            print("Aucun contact à trier.")
    except Exception as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"Erreur lors du tri des contacts : {e}")

def travail_termine():
    print("Travail terminé !!!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    import webbrowser

    url = "https://media0.giphy.com/media/m2Q7FEc0bEr4I/giphy.gif?cid=6c09b952uueqiuxqbkf9wh0dm0rdk5ow9qtjn5l3dk2ifw0q&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    webbrowser.open(url)