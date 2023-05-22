# 📋 Flask

Welcome on my repo

Le but est de développer un script en python, permettant d'afficher un formulaire de contact et de traiter sa réponse: sanitisation, validation, puis envoi et feedback à l'utilisateur




## Authors

- [@Cowez](https://github.com/Cowez)
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/benjamin-cowez/)



## Objectifs

- Si l'utilisateur commet une erreur, lui retourner le formulaire, avec les réponses valides remises dans leurs inputs respectifs.
- Le formulaire effectuera un nettoyage (sanitization) et une validation serverside
- Si la sanitization et la validation sont ok, une page "Merci de nous avoir contacté." s'affichera avec un résumé de l'ensemble des informations encodées.
- Implémentation de la technique antispam du honeypot.
## Instructions

Le formulaire doit contenir : 
- prénom & nom + email + pays (liste)
- message + genre (H/F) + 3 sujets possibles ((Réparation, Commande, Autres)
- Tous les champs sont obligatoires, sauf le sujet (dans ce cas, valeur = "Autre")
