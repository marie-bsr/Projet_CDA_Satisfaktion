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

@app.route('/login')
def page_de_login():
    return render_template("connection.html")

@app.route('/accueil')
def page_accueil():
    return render_template("Index.html", nom="Anthony")


if __name__ == '__main__':
    app.run(debug=True)
