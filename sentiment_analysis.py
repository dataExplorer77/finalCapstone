
# Importing packages needed for script
import numpy as np
import pandas as pd
import spacy

# Loading SpaCy package
nlp = spacy.load("en_core_web_sm")

# Storing a pandas copy of the data in a variable, in preparation of preprocessing data
amazon_data = pd.read_csv('amazon_product_reviews.csv')

# Isolating the "reviews" column
reviews_data = amazon_data["reviews.text"]

# Dropping NaN values
cleaned_data = reviews_data.dropna(inplace = True, axis=0)






print(reviews_data.head())