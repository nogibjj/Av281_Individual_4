from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Set up the text generation pipeline with GPT-2 model
pipe = pipeline("text-classification")


@app.route("/")
def index():
    return render_template("input.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        input_text = request.form["prompt"]

        # Construct the prompt sentence
        prompt = f"{input_text}"

        # Generate text using GPT-2 based on the constructed prompt
        Answer = pipe(prompt)

        # Extract the generated texts excluding the original prompt
        Sentiment = Answer[0]['label']

        return render_template(
            "sentiments.html", sentiment=Sentiment
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
