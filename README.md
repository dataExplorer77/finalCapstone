# NLP Applications

This repository is for a HyperionDev capstone project in which I use Python code to 
conduct NLP sentiment analysis of a dataset of Amazon product reviews to help establish
if the sentiment of the product reviews is positive, negative or neutral. The program
also has a feature that compares the similarities between two reviews.



## Table of contents

- Instalation instructions
- How to use
- Credits



## Instalation instructions

1. Install the latest version of Python.

2. Clone this project's repository using the following command:
   
   git clone https://github.com/dataExplorer77/finalCapstone

4. Install the required packages:
   - pandas
   - spacy
   - textblob

5. Download the SpaCy model:
   
   -m spacy download en_core_web_sm"



## How to use

### First, the program creates a pandas data frame from an Amazon reviews CSV file.

![Creating Pandas Data Frame](https://github.com/dataExplorer77/finalCapstone/blob/main/Creating%20Pandas%20Data%20Frame.jpg?raw=true)


### The program then uses Spacy to clean and preprocess the data.  

![Cleaning & Preprocessing The Data](https://github.com/dataExplorer77/finalCapstone/blob/main/Cleaning%20&%20Preprocessing%20The%20Data.jpg?raw=true)


### The program then uses TextBlob for sentiment analysis, based on polarity. 

![Applying Sentiment Analysis](https://github.com/dataExplorer77/finalCapstone/blob/main/Cleaning%20&%20Preprocessing%20The%20Data.jpg?raw=true)


### A test is then done to test the accuracy of the sentiment analysis.

![Testing Accuracy of Sentiment Analysis](https://github.com/dataExplorer77/finalCapstone/blob/main/Testing%20Accuracy%20of%20Sentiment%20Analysis.jpg?raw=true)


### The last feature of the program uses SpaCy to compare the similarities between the two reviews.

![Testing Accuracy of Sentiment Analysis](https://github.com/dataExplorer77/finalCapstone/blob/main/Comparing%20Similarity.jpg?raw=true)



## Credits

Danial Albiston created this program
