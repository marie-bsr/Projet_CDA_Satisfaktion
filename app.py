#! /usr/bin/python
# -*- coding:utf-8 -*-
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, request, redirect, url_for, render_template, session
from flask_login import LoginManager, login_required
from flask_login import UserMixin, login_user, current_user
from form import LoginForm
from pprint import pprint
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
app = Flask(__name__)

cnx = mysql.connector.connect(
    host="da.cefim-formation.org",
    user="MGMO_CDA",
    passwd="MGMO",
    database="MGMO_CDA"
)

# Création de l'objet qui permet de dialoguer avec la base
mycursor = cnx.cursor()

login = LoginManager(app)
# requete pour recupérer toutes les info d'une table

#connexion à la BDD
#requete pour recupérer 1 info d'une table
def mafonctioncompteur (codeSql) :
    cursor = cnx.cursor()
    cursor.execute(codeSql) 
    compteur = []
    compteur=cursor.fetchone()[0]
    #for entry in cursor:
    #    compteur.append(entry)
    return compteur


def getTable(table_name):
    cursor = cnx.cursor(dictionary=True)
    sql = (f"SELECT * FROM {table_name}")
    cursor.execute(sql)
    values = []
    for entry in cursor:
        values.append(entry)
    return values

#Requete pour mettre en place les données pour les graphiques
def getQuantiArray(rep):    
    cursor = cnx.cursor()
    requete = (f'SELECT {rep} FROM questionnaire_quanti')
    cursor.execute(requete)
    constructor = [0, 0, 0, 0, 0]
    for data in cursor:
        if data[0] == "Très insuffisant":
            constructor[0] += 1
        if data[0] == "Insatisfaisant":
            constructor[1] += 1
        if data[0] == "Acceptable":
            constructor[2] += 1
        if data[0] == "Satisfaisant":
            constructor[3] += 1
        if data[0] == "Excellent":
            constructor[4] += 1
    return(constructor)

# Variables globales
hash = generate_password_hash('admin')
formations = getTable("formation")
users = getTable("utilisateur")
roles = getTable('role')
formations = getTable('formation')
etudiants = getTable('etudiant')



@app.route('/')
def index():
    return redirect(url_for('page_de_login'))


@app.route('/login', methods=['GET', 'POST'])
def page_de_login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin@admin.admin' or request.form['password'] != 'admin':
            error = 'Identifiants invalides, veuillez réessayer.'
        else:
            return redirect(url_for('page_accueil'))

    return render_template("connection.html", connected=0, error=error, profil={})


@app.route('/accueil')
def page_accueil():
    return render_template("page.html",connected = 1, formations=formations,profil={"nom": "Anthony", "role": "admin"})


@app.route('/promotion/<promotion>')
def page_promo(promotion):
    promo = eval(promotion)
    results = getQuantiArray("rep_methodes")
    results_progress = getQuantiArray("rep_progression")
    return render_template("dashboard.html",connected = 1, promotion=promo, methodes=results, progress= results_progress, profil={"nom": "Anthony", "role": "admin"})

# ADMIN
@app.route('/admin')
def page_admin():
    return render_template("admin.html", connected = 1,profil={"nom": "Anthony", "role": "admin"}, admin_type="administrateur")


@app.route('/admin/utilisateurs')
def admin_utilisateurs():
    return render_template("admin.html", connected = 1,utilisateurs=users, formations=formations, roles=roles, profil={"nom": "Anthony", "role": "admin"}, admin_type="utilisateurs")


@app.route('/admin/formations')
def admin_formations():
    return render_template("admin.html",connected = 1, formations=formations, profil={"nom": "Anthony", "role": "admin"}, admin_type="formations")


@app.route('/admin/etudiants')
def admin_etudiants():
    return render_template("admin.html", connected = 1,etudiants=etudiants, formations=formations, profil={"nom": "Anthony", "role": "admin"}, admin_type="étudiants")

#Route tests marie
@app.route('/pie')
def pie():
    results = getQuantiArray('rep_methodes')
    pprint(results)
    return render_template('pie.html', results=results)


#Route tests Gwen
@app.route('/graphique')
def page_graph () :
    tab_compteur = getQuantiArray("rep_progression")
    tab_compteur=[0, 0, 0, 0, 0]
    #récupération des étiquettes
    cursor = cnx.cursor(dictionary=True)
    sql = ("SELECT DISTINCT rep_progression  FROM questionnaire_quanti")
    cursor.execute(sql) 
    values = []
    for entry in cursor:
        values.append(entry)

    return render_template(
        "graphGwen.html", 
        resultetiquette = values,
        results=tab_compteur
    )

if __name__ == '__main__':
    app.run(debug=True)

