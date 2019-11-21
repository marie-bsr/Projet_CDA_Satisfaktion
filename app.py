#! /usr/bin/python
# -*- coding:utf-8 -*-
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, request, redirect, url_for, render_template
from pprint import pprint
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


#requete pour recupérer toutes les info d'une table
def getTable(table_name):
    cursor = cnx.cursor(dictionary=True)
    sql = (f"SELECT * FROM {table_name}")
    cursor.execute(sql) 
    values = []
    for entry in cursor:
        values.append(entry)
    return values


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

    return render_template("connection.html",connected=0, error=error, profil={})


@app.route('/accueil')
def page_accueil():
    formations = getTable("formation")
    return render_template("page.html", formations=formations, connected=1, profil={"nom": "Anthony", "role": "admin"})


@app.route('/promotion/<promotion>')
def page_promo(promotion):
    promo = eval(promotion)
    print(promo)
    return render_template("dashboard.html", promotion = promo, connected=1, profil={"nom": "Anthony", "role": "admin"})

# ADMIN
@app.route('/admin')
def page_admin():
    return render_template("admin.html", connected=1, profil={"nom": "Anthony", "role": "admin"}, admin_type="administrateur")


@app.route('/admin/utilisateurs')
def admin_utilisateurs():
    return render_template("admin.html", connected=1, profil={"nom": "Anthony", "role": "admin"}, admin_type="utilisateurs")


@app.route('/admin/formations')
def admin_formations():
    return render_template("admin.html", connected=1, profil={"nom": "Anthony", "role": "admin"}, admin_type="formations")


@app.route('/admin/etudiants')
def admin_etudiants():
    return render_template("admin.html", connected=1, profil={"nom": "Anthony", "role": "admin"}, admin_type="étudiants")


if __name__ == '__main__':
    app.run(debug=True)
