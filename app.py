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


def getTable(table_name):
    cursor = cnx.cursor(dictionary=True)
    sql = (f"SELECT * FROM {table_name}")
    cursor.execute(sql)
    values = []
    for entry in cursor:
        values.append(entry)
    return values


# Variables globales
hash = generate_password_hash('admin')
formations = getTable("formation")
users = getTable("utilisateur")
roles = getTable('role')
formations = getTable('formation')
etudiants = getTable('etudiant')

@app.route('/')
def index():
    return redirect(url_for('page_accueil'))


@app.route('/login', methods=['GET', 'POST'])
def page_de_login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin@admin.admin' or request.form['password'] != 'admin':
            error = 'Identifiants invalides, veuillez réessayer.'
        else:
            return redirect(url_for('page_accueil'))

    return render_template("connection.html", connected=0, error=error)


@app.route('/accueil')
def page_accueil():
    return render_template("page.html",connected = 1, formations=formations,profil={"nom": "Anthony", "role": "admin"})


@app.route('/promotion/<promotion>')
def page_promo(promotion):
    promo = eval(promotion)
    return render_template("dashboard.html",connected = 1, promotion=promo,  profil={"nom": "Anthony", "role": "admin"})

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


if __name__ == '__main__':
    app.run(debug=True)




def getData1():

    requete = "SELECT COUNT(rep_methodes) FROM questionnaire_quanti WHERE rep_methodes='Très insuffisant'"
    cursor = connection.cursor()
    cursor.execute(requete)
    result = cursor.fetchone()[0]
    return(result)

def getData2():

    requete = "SELECT COUNT(rep_methodes) FROM questionnaire_quanti WHERE rep_methodes='Insatisfaisant'"
    cursor = connection.cursor()
    cursor.execute(requete)
    result = cursor.fetchone()[0]
    return(result)

def getData3():

    requete = "SELECT COUNT(rep_methodes) FROM questionnaire_quanti WHERE rep_methodes='Acceptable'"
    cursor = connection.cursor()
    cursor.execute(requete)
    result = cursor.fetchone()[0]
    return(result)

def getData4():

    requete = "SELECT COUNT(rep_methodes) FROM questionnaire_quanti WHERE rep_methodes='Satisfaisant'"
    cursor = connection.cursor()
    cursor.execute(requete)
    result = cursor.fetchone()[0]
    return(result)

def getData5():

    requete = "SELECT COUNT(rep_methodes) FROM questionnaire_quanti WHERE rep_methodes='Excellent'"
    cursor = connection.cursor()
    cursor.execute(requete)
    result = cursor.fetchone()[0]
    return(result)


@app.route('/pie')
def pie():
    results = [getData1(),getData2(),getData3(),getData4(),getData5()]
   
    return render_template('pie.html', results=results)
