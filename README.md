# Food Recommendation System

A machine learning system that recommends dishes using multiple search option like search by cuisine, course or dish. The system provides visual recommendations with images and detailed information.

## Key Features

- **Multiple Search Options**:
  - By cuisine (Indian, American, Mexican etc.)
  - By course (Main Course, Dessert, Breakfast etc.)
  - By specific dish name (Biryani, Pizza, Pasta etc.)
  
- **Visual Recommendations**:
  - Displays top 3 matching recipes
  - Shows dish images in a responsive grid
  - Clean, user-friendly interface

- **Technical Features**:
  - Built with Python and Streamlit
  - Uses KNN algorithm for recommendations
  - Sentence Transformers for text embeddings
  - Comprehensive logging system

## System Architecture

1. **Data Collection**:
   - Web scraper collects recipes from vegrecipesofindia.com
   - Extracts: dish name, image URL, cuisine, course, dietary info
   - Stores in CSV format (`data/recipe_data_processed.csv`)

2. **Machine Learning**:
   - Pre-trained sentence transformer model (`models/embedding_model.pkl`)
   - KNN model for similarity search (`models/knn_model.pkl`)
   - Processes user queries into embeddings
   - Finds nearest neighbors in recipe space

3. **Web Interface**:
   - Streamlit-based UI
   - Responsive design
   - Real-time recommendations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Food-Recommendation-System.git
cd Food-Recommendation-System
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download pre-trained models from the 'models/' directory.

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. In the web interface:
   - Type your search query (cuisine, course or dish name)
   - Click "Search" button
   - View recommendations

Example searches:
- "Indian"
- "Dessert" 
- "Pasta"

## Dependencies

- Python 3.8+
- Streamlit
- Pandas
- Scikit-learn
- Sentence-transformers
- Selenium (for scraper)
