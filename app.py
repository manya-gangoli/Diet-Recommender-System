from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Global variables for the DataFrame and scaler
df = None
scaler = None

def load_data():
    global df, scaler
    df = pd.read_csv('All_Diets.csv')
    
    # Remove duplicates and preprocess
    df.drop_duplicates(inplace=True)
    df.drop_duplicates(subset=['Recipe_name', 'Protein(g)', 'Carbs(g)', 'Fat(g)'], keep='first', inplace=True)
    df.drop(['Extraction_day', 'Extraction_time'], axis=1, inplace=True)
    
    scaler = MinMaxScaler()
    df[['Protein(g)', 'Carbs(g)', 'Fat(g)']] = scaler.fit_transform(df[['Protein(g)', 'Carbs(g)', 'Fat(g)']])

# Load data when the app starts
load_data()

# Recommendation function
def recommend_recipes(user_protein, user_carbs, user_fat, ingredient=None, diet_type=None, cuisine_type=None, top_n=5):
    global df, scaler
    if df is None or scaler is None:
        load_data()

    user_input = np.array([[user_protein, user_carbs, user_fat]])
    user_input_normalized = scaler.transform(user_input)

    # Filter dataset
    filtered_df = df.copy()
    if diet_type:
        filtered_df = filtered_df[filtered_df['Diet_type'] == diet_type]
    if cuisine_type:
        filtered_df = filtered_df[filtered_df['Cuisine_type'] == cuisine_type]
    if ingredient:
        filtered_df = filtered_df[filtered_df['Recipe_name'].str.contains(ingredient, case=False, na=False)]

    if filtered_df.empty:
        return []

    # Compute similarity
    similarity_scores = cosine_similarity(user_input_normalized, filtered_df[['Protein(g)', 'Carbs(g)', 'Fat(g)']])[0]
    filtered_df['Similarity'] = similarity_scores
    recommended_recipes = filtered_df.sort_values(by='Similarity', ascending=False)

    # Return results
    return recommended_recipes[['Recipe_name', 'Diet_type', 'Cuisine_type', 'Similarity']].head(top_n).to_dict('records')

# API endpoint for recommendations
@app.route('/recommend', methods=['POST'])
def get_recommendations():
    try:
        data = request.json
        user_protein = float(data['protein'])
        user_carbs = float(data['carbs'])
        user_fat = float(data['fat'])
        ingredient = data.get('ingredient')
        diet_type = data.get('dietType')
        cuisine_type = data.get('cuisineType')

        # Get recommendations
        recommendations = recommend_recipes(user_protein, user_carbs, user_fat, ingredient, diet_type, cuisine_type)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def hello():
    return "Hello, Recipe Recommender!"

if __name__ == '__main__':
    app.run(debug=True)