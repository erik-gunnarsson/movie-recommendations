from flask import Flask, render_template, request
import openai_secret_manager
import openai

app = Flask(__name__)

# Set up OpenAI API key and model
import openai 
openai.api_key = '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'

model_engine = "GPT-3"

# Set up prompt
model_prompt = (f"Please suggest 5 movies similar to the following two movies. Your response should be a bullet point list stating Movie Name - Director - release date and should have no other comments:\n"
                f"1. {movie_1}\n"
                f"2. {movie_2}\n")


# Define a function to generate movie recommendations
def generate_movie_recommendations(movie_inputs):
    prompt = model_prompt.format(movie_1=movie_inputs[0], movie_2=movie_inputs[1])
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.1,
    )
    message = response.choices[0].text.strip()
    return message.split("\n")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        movie_1 = request.form.get("movie1")
        movie_2 = request.form.get("movie2")
        movie_inputs = [movie_1, movie_2]
        recommendations = generate_movie_recommendations(movie_inputs)
        return render_template("index.html", recommendations=recommendations)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()
