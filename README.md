Document Reader vous permet d'extraire à partir d'une image les informations de documents d'identité ou d'une carte de crédit/débit.
La fonction d'extration des informations est pour l'instant sommaire mais l'objectif est de pouvoir l'améliorer pour que cela marche en dehors des documents de tests et les spécimens.
Le but principal de cette première version est de traiter le document soumis par l'utilisateur et de lui afficher l'information en retour dans une application web, ici grace au framework Flask et au langage Python.

INSTALLATION
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt

export FLASK_APP=webapp.py
flask run
