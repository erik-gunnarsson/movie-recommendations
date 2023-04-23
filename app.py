import openai 

openai.api_key = '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'

# Set up OpenAI Davinci model
model_engine = "GPT-3"
model_prompt = (f"Please suggest 5 movies similar to the following two movies. Your response should be a bullet point list stating Movie Name - Director - release date and should have no other comments:\n"
                f"1. {movie_1}\n"
                f"2. {movie_2}\n")

# Define a function to generate movie recommendations
def generate_movie_recommendations(movie_inputs):
    movie_1, movie_2 = movie_inputs
    prompt = model_prompt.format(movie_1=movie_1, movie_2=movie_2)
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

# Test the function with sample inputs
movie_1 = "Cars"
movie_2 = "Kung Fu Panda"
movie_inputs = [movie_1, movie_2]
recommendations = generate_movie_recommendations(movie_inputs)
display(recommendations)

