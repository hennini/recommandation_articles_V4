import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Remplacez cette URL par l'URL de votre fonction Azure
AZURE_FUNCTION_URL = 'http://localhost:7071/api/reco_api_V4'

@app.route('/', methods=['GET', 'POST'])  # Accepter les méthodes GET et POST
def get_recommendations():
    user_id = None
    recommended_articles = []  # Pour stocker les articles recommandés

    if request.method == 'POST':  # Vérifier si la requête est un POST
        try:
            user_id = int(request.form['userid'])  # Récupérer l'ID utilisateur depuis le formulaire
            # Faire la requête GET à la fonction Azure
            response = requests.get(f"{AZURE_FUNCTION_URL}?name={user_id}")
            response.raise_for_status()  # Vérifier s'il y a eu des erreurs HTTP

            # Extraire les données JSON de la réponse
            data = response.json()
            recommended_articles = data.get('recommended_articles', [])

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête : {e}")
            recommended_articles = []  # Si une erreur survient, définir comme vide
        except ValueError:
            print("ID utilisateur non valide.")
            recommended_articles = []

    # Passer uniquement les articles recommandés au template
    return render_template('index.html', user_id=user_id, recommendations=recommended_articles)

if __name__ == '__main__':
    app.run(debug=True)
