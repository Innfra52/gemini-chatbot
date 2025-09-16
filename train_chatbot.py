import json
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import pickle

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the intents file
try:
    with open('intents.json') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: 'intents.json' not found. Please make sure the file is in the same directory.")
    exit()

# Prepare data for training
words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']

for intent in data['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # Add documents in the corpus
        documents.append((word_list, intent['tag']))
        # Add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and lowercase each word, and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# Sort classes
classes = sorted(list(set(classes)))

print(f"Words: {words}")
print(f"Classes: {classes}")

# Create training data
X = []
y = []

for doc in documents:
    # Bag of words
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    for w in words:
        bag.append(1 if w in word_patterns else 0)

    X.append(bag)
    y.append(doc[1]) # Directly append the intent tag

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Save the model
model_data = {
    'model': model,
    'words': words,
    'classes': classes
}
with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

print("Model trained and saved!")