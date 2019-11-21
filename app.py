#! /usr/bin/python
# -*- coding:utf-8 -*-

from mysql.connector import Error
import mysql.connector
from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

connection = mysql.connector.connect(
    host="da.cefim-formation.org",
    user="MGMO_CDA",
    passwd="MGMO",
    database="MGMO_CDA"
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

    return render_template("connection.html", connected=0, error=error)


@app.route('/accueil')
def page_accueil():
    return render_template("page.html", connected=1, profils={"nom": "Anthony", "role": "admin"})


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
