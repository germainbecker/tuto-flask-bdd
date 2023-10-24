from flask import Flask, render_template, request

from bdd import recuperer_eleves_par_nom, recuperer_eleves

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Bienvenue sur mon site !</h1>"

@app.route("/recherche", methods=['GET', 'POST'])
def recherche():
    if request.method == "POST":
        # si le formulaire est envoyé
        donnees = request.form
        nom = donnees.get('nom')
        liste_eleves = recuperer_eleves(nom)
        print(liste_eleves)

    else:
        # méthode GET
        liste_eleves = None
    return render_template("recherche.html", eleves=liste_eleves)