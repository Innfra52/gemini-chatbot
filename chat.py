import pickle
import numpy as np
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

# Load the trained model and data
with open('chatbot_model.pkl', 'rb') as f:
    model_data = pickle.load(f)
model = model_data['model']
words = model_data['words']
classes = model_data['classes']

# Load the intents file
with open('intents.json') as file:
    intents = json.load(file)

lemmatizer = WordNetLemmatizer()

def clean_up_sentence(sentence):
    """Tokenize and lemmatize the user's sentence."""
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words):
    """Create a bag-of-words array for the model."""
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    """Predict the intent class of the user's message."""
    p = bag_of_words(sentence, words)
    res = model.predict([p])[0]
    return res

def get_response(tag, intents_json):
    """Get a random response based on the predicted intent tag."""
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response

# Main chat loop
print("Chatbot is ready! You can start talking.")
while True:
    message = input("You: ")
    if message.lower() == "quit":
        break

    predicted_tag = predict_class(message)
    response = get_response(predicted_tag, intents)
    print("Bot:", response)