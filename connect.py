from __future__ import print_function

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pprint

import mysql.connector
from mysql.connector import errorcode

from datetime import datetime

# Créé les autorisations d'accès
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('satisfaktion_secret.json', scope)
client = gspread.authorize(creds)

# Créé la feuille de données sur la base du tableau Excel
sheet = client.open('questionnaire_data').sheet1

# Met en forme les données récupérées
pp = pprint.PrettyPrinter()

# Permet de sélectionner tout ou partie des données
satisfaktion = sheet.get_all_records()

try:
        # création de l'objet connection
        cnx = mysql.connector.connect(
                host="da.cefim-formation.org",
                user="MGMO_CDA",
                passwd="MGMO",
                database="MGMO_CDA"
        )

        # Création de l'objet qui permet de dialoguer avec la base
        mycursor = cnx.cursor()

        # Sélection des valeurs par colonne dans le tableau excel
        dataA = [datetime.strptime(line['date'], "%d/%m/%Y %H:%M:%S") for line in satisfaktion[1:]]
        dataB = [line['nom'] for line in satisfaktion[1:]]
        dataC = [line['prenom'] for line in satisfaktion[1:]]
        dataD = [line['methode'] for line in satisfaktion[1:]]
        dataE = [line['progression'] for line in satisfaktion[1:]]
        dataF = [line['organisation'] for line in satisfaktion[1:]]
        dataG = [line['pedago'] for line in satisfaktion[1:]]
        dataH = [line['echange'] for line in satisfaktion[1:]]
        dataI = [line['faible'] for line in satisfaktion[1:]]
        dataJ = [line['fort'] for line in satisfaktion[1:]]
        dataK = [line['comment'] for line in satisfaktion[1:]]
        dataL = [line['promo'] for line in satisfaktion[1:]]

        # Requêtes de vérification des doublons
        verif1 = "SELECT COUNT(*) FROM etudiant WHERE nom=%s AND prenom=%s AND formation_id=%s"
        verif2 = "SELECT COUNT(*) FROM questionnaire_quanti WHERE date_reponse=%s AND rep_methodes=%s AND rep_progression=%s AND rep_organisation=%s AND rep_pedago=%s AND rep_echanges=%s AND id_etudiant=%s"
        verif3 = "SELECT COUNT(*) FROM questionnaire_quali WHERE date_reponse=%s AND rep_point_faible=%s AND rep_point_fort=%s AND rep_commentaire=%s AND etudiant=%s"

        # Requêtes d'insertion des données dans Mysql
        sql1 = "INSERT INTO etudiant (nom, prenom, formation_id) VALUES (%s, %s, %s)"
        sql2 = "INSERT INTO questionnaire_quanti (date_reponse, rep_methodes, rep_progression, rep_organisation, rep_pedago, rep_echanges, id_etudiant) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        sql3 = "INSERT INTO questionnaire_quali (date_reponse, rep_point_faible, rep_point_fort, rep_commentaire, etudiant) VALUES (%s, %s, %s, %s, %s)"

        # Balaye les données par index pour compléter les tables ligne par ligne
        for i in range(len(dataB)):

                # Insertion des données dans la table etudiant
                val1 = (dataB[i], dataC[i], dataL[i])
                # vérifie si la ligne insérée existe déjà dans la table
                mycursor.execute(verif1, val1)
                # insère les données si OK
                if mycursor.fetchone()[0] == 0:
                        mycursor.execute(sql1, val1)

                # Sélection l'id de l'étudiant inséré dans la table
                query_id_etudiant = ("SELECT id FROM etudiant WHERE nom=%s AND prenom=%s LIMIT 1")
                mycursor.execute(query_id_etudiant, (dataB[i], dataC[i]))
                
                # Boucle sur chaque étudiant entré dans la table via l'id
                for id in mycursor:
                        id_etudiant = id[0]

                # Insertion des données dans la table questionnaire_quanti avec id-etudiant
                val2 = (dataA[i], dataD[i], dataE[i], dataF[i], dataG[i], dataH[i], id_etudiant)
                # vérifie si la ligne insérée existe déjà dans la table
                mycursor.execute(verif2, val2)
                # insère les données si OK
                if mycursor.fetchone()[0] == 0:
                        mycursor.execute(sql2, val2)

                # Insertion des données dans la table questionnaire_quali avec id-etudiant
                val3 = (dataA[i], dataI[i], dataJ[i], dataK[i], id_etudiant)
                # vérifie si la ligne insérée existe déjà dans la table
                mycursor.execute(verif3, val3)
                # insère les données si OK
                if mycursor.fetchone()[0] == 0:
                        mycursor.execute(sql3, val3)
        
        # Exécute les instructions liées à la connexion
        cnx.commit()

        mycursor.close()

# Gère les erreurs de connexion
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)
else:
        cnx.close()

