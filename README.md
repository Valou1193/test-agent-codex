# test-agent-codex
premier projet codex pour automatiser des recherches leboncoin

## Simulation d'appel téléphonique
Ce dépôt inclut un script Flask qui simule un appel téléphonique.
Il utilise Google Text-to-Speech pour générer la réponse vocale
à une question typique de client de restaurant.

### Lancer l'application
1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Démarrez le serveur Flask :
   ```bash
   FLASK_APP=app.py flask run
   ```
3. Visitez `http://localhost:5000/call` pour écouter la réponse.
