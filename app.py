from flask import Flask, render_template, request, url_for
import re

# création de l'application
app = Flask(__name__)

# créé une route pour accéder à mon serveur temp et accéder à la page "Home"
@app.route('/') 
def home():
    return render_template('index.html')

# page de validation
@app.route('/retour', methods=['POST']) 

# Définition de la fonction de validation des données du formulaire
def form_valide():
    # Fonction auxiliaire pour valider l'adresse email
    def email_valide(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)
    
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    email = request.form.get('email')
    pays = request.form.get('pays')
    genre = request.form.get('genre')
    message = request.form.get('message')
    sujets = request.form.get('sujets')

    # Vérification des caractères dans "nom" et "prenom"
    if not re.match(r'^[A-Za-zÀ-ÿ\s-]+$', nom) or not re.match(r'^[A-Za-zÀ-ÿ\s-]+$', prenom):
        return "Le nom et le prénom doivent contenir uniquement des lettres ou être rempli."

    # Vérification de l'adresse email
    if not email_valide(email):
        return "Veuillez indiquer une adresse mail"

    # Vérification des champs obligatoires (nom, prenom, email, pays, genre, message)
    if not nom or not prenom or not email or not pays or not genre or not message:
        return "Veuillez remplir tous les champs du formulaire."

    return render_template('retour.html', prenom = prenom, nom = nom, email = email, pays = pays, genre = genre, message = message, sujets = sujets )

# Lancement de l'app via le terminal
if __name__ == "__main__":
    app.run(debug=True)
