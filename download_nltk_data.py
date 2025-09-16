import nltk
try:
    nltk.download('punkt')
    nltk.download('wordnet')
    print("NLTK data download successful!")
except Exception as e:
    print(f"An error occurred: {e}")