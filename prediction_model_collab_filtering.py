import pandas as pd
import pickle
import numpy as np
import json

articles_df = pd.read_csv("articles_metadata.csv")
#print(articles_df.head())

#print('hi')


# Save to file in the current working directory

pkl_filename = "pickle_surprise_model_KNNWithMeans.pkl"

# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

#print(pickle_model)

def predict_best_category_for_user(user_id, model, article_df):
    predictions = {}
    
    #Category 1 to 460
    for i in range(1, 460):
        _, cat_id, _, est, err = model.predict(user_id, i)
        
        #Keep prediction only if we could keep it.
        if (err != True):
            predictions[cat_id] = est
    
    best_cats_to_recommend = dict(sorted(predictions.items(), key=lambda x: x[1], reverse=True)[:5])
    
    # Obtenir les articles recommandés pour chaque catégorie
    recommended_articles = []
    for key, _ in best_cats_to_recommend.items():
        article_id = int(articles_df[articles_df['category_id'] == key]['article_id'].sample(1).values)
        recommended_articles.append({
            "category_id": key,
            "article_id": article_id
        })
    
    # Créer un dictionnaire pour la sortie JSON
    output = {
        "user_id": user_id,
        "recommended_articles": recommended_articles,
        "best_categories": best_cats_to_recommend
    }
    
    # Retourner le dictionnaire au format JSON
    return json.dumps(output, indent=4)


results = predict_best_category_for_user(1, pickle_model, articles_df)

print(results)