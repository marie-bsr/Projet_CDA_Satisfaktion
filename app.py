#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

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
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Identifiants invalides, veuillez réessayer.'
        else:
            return redirect(url_for('page_accueil'))

    return render_template("connection.html", connected = 0, error = error)


@app.route('/accueil')
def page_accueil():
    return render_template("page.html", connected = 1, profils = {"nom" : "Anthony", "role" : "admin"})


if __name__ == '__main__':
    app.run(debug=True)
