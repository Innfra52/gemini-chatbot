import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

# Replace with your actual API key
genai.configure(api_key="AIzaSyBBNX-CD-gH74vEFM2toa1YIDp5w_RFeGg")

app = Flask(__name__)

# Create a Gemini model instance
model = genai.GenerativeModel('gemini-1.5-flash-latest')
chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    user_input = request.json.get("message")

    # Start a new chat session to maintain conversation history
    chat = model.start_chat(history=chat_history)

    try:
        response = chat.send_message(user_input)
        gemini_response = response.text
        chat_history = chat.history
        return jsonify({"response": gemini_response})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"response": "An error occurred. Please try again."})

if __name__ == "__main__":
    app.run(debug=True)