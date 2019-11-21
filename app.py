#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

import mysql.connector
from mysql.connector import Error

#connexion à la BDD
try:
    connection = mysql.connector.connect(host='da.cefim-formation.org',
                                         database='MGMO_CDA',
                                         user='MGMO_CDA',
                                         password='MGMO')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        #cursor.close()
        #connection.close()
        print("MySQL connection is closed")

#requete pour recupérer toutes les info d'une table
def getTable(table_nom) :
    cursor = connection.cursor(dictionary=True)
    sql = (f"SELECT * FROM {table_nom}")
    cursor.execute(sql) 
    values = []
    for entry in cursor:
        values.append(entry)
    return values

def mafonctioncompteur (codeSql) :
    cursor = connection.cursor()
    cursor.execute(codeSql) 
    compteur = []
    compteur=cursor.fetchone()[0]
    #for entry in cursor:
    #    compteur.append(entry)
    return compteur


#page graphique Gwen
@app.route('/graphique')
def page_graph () :

    tab_compteur=[0, 0, 0, 0, 0]
    #récupération des étiquettes
    cursor = connection.cursor(dictionary=True)
    sql = ("SELECT DISTINCT rep_progression  FROM questionnaire_quanti")
    cursor.execute(sql) 
    values = []
    for entry in cursor:
        values.append(entry)

    #récupère la liste des acceptable
    sql_accep = ("SELECT COUNT(id) FROM questionnaire_quanti WHERE rep_progression='Acceptable' ")
    tab_compteur[2] = mafonctioncompteur(sql_accep)
    #récupère la liste des insatisfaisant
    sql_insatisf = ("SELECT COUNT(id) FROM questionnaire_quanti WHERE rep_progression='Insatisfaisant' ")
    tab_compteur[1]=mafonctioncompteur(sql_insatisf)
    #récupère la liste des excellent
    sql_excell = ("SELECT COUNT(id) FROM questionnaire_quanti WHERE rep_progression='Excellent'")
    tab_compteur[4]=mafonctioncompteur(sql_excell)
    #récupère le nombre de insuffisant   
    sql_insuff= ("SELECT COUNT(id) FROM questionnaire_quanti WHERE rep_progression='Très insuffisant'")
    tab_compteur[0]=mafonctioncompteur(sql_insuff)
    #récupère la liste des satisfaisant
    sql_satisf= ("SELECT COUNT(id) FROM questionnaire_quanti WHERE rep_progression='Satisfaisant'")
    tab_compteur[3]=mafonctioncompteur(sql_satisf)
    return render_template(
        "graphGwen.html", 
        resultetiquette = values,
        results=tab_compteur
    )

@app.route('/')
def index():
    return "Bonjour, vous êtes situé a la racine "


@app.route('/profil')
def profil(utilisateur_non_identifie):
    if utilisateur_non_identifie:
        return(redirect(url_for('page_de_login')))
    else:
        return(redirect(url_for('page_accueil')))

# @app.route('/login')
# def page_de_login():
#     return render_template("connection.html", connected = 0)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin@admin.admin' or request.form['password'] != 'admin':
            error = 'Identifiants invalides, veuillez réessayer.'
        else:
            return redirect(url_for('page_accueil'))

    return render_template("connection.html", connected = 0, error = error)


@app.route('/accueil')
def page_accueil():
    return render_template("page.html", connected = 1, profils = {"nom" : "Anthony", "role" : "admin"})


if __name__ == '__main__':
    app.run(debug=True)



#page graphique Gwen camembert
@app.route('/graphique_camembert')
def page_graph2 () :
    return render_template("graphGwen2.html")