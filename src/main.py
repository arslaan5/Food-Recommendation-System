import pandas as pd
import pickle
from src.logger import logger
from src.exception import CustomException
import sys


pd.set_option('display.max_colwidth', None)

# Read the data
try:
    df = pd.read_csv(r"data/recipe_data_processed.csv")
    logger.info("Data loaded successfully.")
except Exception as e:
    logger.error("Data loading failed")
    raise CustomException(e,sys)

# Load the pre-trained embedding model
try:
    embedding_model = pickle.load(open("models/embedding_model.pkl", "rb"))
    logger.info("Embedding model successfully loaded.")
except Exception as e:
    logger.error("Embedding model loading failed.")
    raise CustomException(e,sys)

# Load the pre-trained KNN model
try:
    knn_model = pickle.load(open("models/knn_model.pkl", "rb"))
    logger.info("KNN model successfully loaded.")
except Exception as e:
    logger.error("KNN model loading failed.")
    raise CustomException(e,sys)

# Function to get the top 3 similar recipes
def recommend_dishes(dish_name, dataframe=df, knn_model=knn_model):
    # Encode the dish name into an embedding
    dish_embedding = embedding_model.encode([dish_name])

    # Find K nearest neighbors
    distances, indices = knn_model.kneighbors(dish_embedding, return_distance=True)

    # Get recommendations
    recommendations = dataframe.iloc[indices[0]][['name', 'imgurl']]
    
    return recommendations

if __name__ == "__main__":
    print(recommend_dishes("pasta"))