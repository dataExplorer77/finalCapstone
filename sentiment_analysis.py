
# Importing packages needed for script
import pandas as pd
import spacy
from textblob import TextBlob


# Loading SpaCy package
nlp = spacy.load("en_core_web_sm")


# Function to preprocess data
def preprocess(text):
    doc = nlp(text.lower().strip())
    return " ".join([token.text for token in doc if not (token.is_stop or token.is_punct)])

# Function to analyze sentiment
def analyze_sentiment(review):
    
    # Using TextBlob for sentiment analysis
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    # Defining sentiment based on polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment


# Creating pandas data frame
amazon_data = pd.read_csv('amazon_product_reviews.csv')


# Isolating the "reviews" column and dropping NaN values
reviews_data = amazon_data["reviews.text"].dropna()

# Creating a new column and applying the preprocessing function     
amazon_data["cleaned_preprocessed_reviews"] = reviews_data.apply(preprocess)


# Creating a new column and applying the sentiment analysis function
amazon_data["sentiment_analysis"] = amazon_data["cleaned_preprocessed_reviews"].apply(analyze_sentiment)


# Testing accuracy of sentiment analysis

pd.set_option('display.max_colwidth', None) # Setting pandas to display entire contents of cells

positive_reviews = amazon_data[amazon_data["sentiment_analysis"] == "positive"]["reviews.text"]
print("Examples of positive reviews:")
print(positive_reviews.head(3))

negative_reviews = amazon_data[amazon_data["sentiment_analysis"] == "negative"]["reviews.text"]
print("\n\nExamples of negative reviews:")
print(negative_reviews.head(3))

neutral_reviews = amazon_data[amazon_data["sentiment_analysis"] == "neutral"]["reviews.text"]
print("\n\nExamples of neutral reviews:")
print(neutral_reviews.head(3))


# Comparing similarity 

comparison_review_1 = nlp(amazon_data["reviews.text"][2])
comparison_review_2 = nlp(amazon_data["reviews.text"][6])

similarity_score = comparison_review_1.similarity(comparison_review_2)

print(f"""
      
The similarity score between review 2 and review 6 = {similarity_score}.

""")
