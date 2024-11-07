from flask import Flask, request, jsonify
import pandas as pd
import pickle
import json

# Initialisation de l'application Flask
app = Flask(__name__)

# Charger les données et le modèle au démarrage de l'application
articles_df = pd.read_csv("articles_metadata.csv")

# Charger le modèle Pickle
pkl_filename = "pickle_surprise_model_KNNWithMeans.pkl"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

# Fonction pour obtenir les meilleures catégories pour l'utilisateur et faire les recommandations
def predict_best_category_for_user(user_id):
    # Dictionnaire pour stocker les prédictions de catégorie
    predictions = {}
    
    # Catégories de 1 à 460
    for i in range(1, 460):
        _, cat_id, _, est, err = pickle_model.predict(user_id, i)
        
        # Si l'estimation est valide, l'ajouter aux prédictions
        if not err:
            predictions[cat_id] = est
    
    # Trier les catégories par score et ne garder que les 5 meilleurs
    best_cats_to_recommend = dict(sorted(predictions.items(), key=lambda x: x[1], reverse=True)[:5])
    
    # Obtenir les articles recommandés pour chaque catégorie
    recommended_articles = []
    for key, _ in best_cats_to_recommend.items():
        article_id = int(articles_df[articles_df['category_id'] == key]['article_id'].sample(1).values)
        recommended_articles.append({
            "category_id": key,
            "article_id": article_id
        })
    
    # Retourner un dictionnaire avec les résultats
    output = {
        "user_id": user_id,
        "recommended_articles": recommended_articles,
        "best_categories": best_cats_to_recommend
    }
    
    return output

# Définir une route pour l'API
@app.route('/reco_api_V4', methods=['GET'])
def reco_api_V4():
    # Récupérer l'ID utilisateur à partir des paramètres de requête
    user_id = request.args.get('userid')
    
    if user_id:
        # Obtenir les recommandations
        recommendations = predict_best_category_for_user(user_id)
        # Retourner le résultat sous forme de JSON
        return jsonify(recommendations), 200
    else:
        # Si l'ID utilisateur est manquant
        return jsonify({"error": "Please provide a userId as a query parameter"}), 400

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
