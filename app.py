#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    print( "Bonjour, vous êtes situé a la racine du site, vous allez être redirigé.")
    return redirect(url_for('page_de_login'))

@app.route('/login', methods=['GET', 'POST'])
def page_de_login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin@admin.admin' or request.form['password'] != 'admin':
            error = 'Identifiants invalides, veuillez réessayer.'
        else:
            return redirect(url_for('page_accueil'))

    return render_template("connection.html", connected = 0, error = error, profil = {})


@app.route('/accueil')
def page_accueil():
    return render_template("page.html", connected = 1, profil = {"nom" : "Anthony", "role" : "admin"})


@app.route('/admin')
def page_admin():
    return render_template("admin.html", connected = 1, profil = {"nom" : "Anthony", "role" : "admin"}, admin_type="administrateur")

@app.route('/admin/utilisateurs')
def admin_utilisateurs():
    return render_template("admin.html", connected = 1, profil = {"nom" : "Anthony", "role" : "admin"}, admin_type="utilisateurs")

@app.route('/admin/formations')
def admin_formations():
    return render_template("admin.html", connected = 1, profil = {"nom" : "Anthony", "role" : "admin"}, admin_type="formations")

@app.route('/admin/etudiants')
def admin_etudiants():
    return render_template("admin.html", connected = 1, profil = {"nom" : "Anthony", "role" : "admin"}, admin_type="étudiants")



if __name__ == '__main__':
    app.run(debug=True)
