from flask import Flask, request, jsonify
from flask_cors import CORS
from qa_logic import answer_question

app = Flask(__name__)
CORS(app) 

@app.route("/")
def home():
    return "Hello! This is the Project Samarth API."

@app.route("/ask", methods=['POST'])
def ask():
    """
    The main API endpoint. Takes a question and returns an answer.
    """

    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided."}), 400


    try:
        answer, sources = answer_question(question)

        
        return jsonify({
            "answer": answer,
            "sources": sources  
        })

    except Exception as e:
      
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000) # Runs the server on http://127.0.0.1:5000