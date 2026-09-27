from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
# for prompt templates.
from langchain_core.prompts import PromptTemplate
model  = init_chat_model (
    "openai/gpt-oss-20b",
    model_provider="groq"
)
prompt = PromptTemplate.from_template("""
You are CineSage, an AI system that processes movie information.

Your task is to analyze the movie description provided below and extract
the most important and useful information from it.

Movie Description:
{movie_text}

Extract the following information:

1. title
   - The name of the movie.

2. year
   - The release year of the movie.
   - If the year is not mentioned, return null.

3. genre
   - Identify the movie's main genres.
   - Return them as a list.

4. director
   - The director of the movie.
   - If the director is not mentioned, return null.

5. main_characters
   - Identify the important characters mentioned in the description.
   - Return them as a list.

6. setting
   - Describe where and when the story takes place.

7. plot
   - Extract the central storyline.
   - Keep it concise and factual.

8. themes
   - Identify the major themes explored in the movie.
   - Return them as a list.

9. summary
   - Generate a clean, easy-to-understand summary of the movie.
   - Keep it between 3 and 5 sentences.
   - Do not include unnecessary details.

Important rules:

- Use ONLY the information provided in the movie description.
- Do not invent or assume information that is not present.
- If information is missing, use null instead of guessing.
- Keep extracted information concise and meaningful.
- Do not include your reasoning or explanation.
- Return ONLY valid JSON.
- Do not use Markdown.
- Do not wrap the JSON inside ```json```.

Return the result using exactly this structure:

{{
    "title": "",
    "year": null,
    "genre": [],
    "director": null,
    "main_characters": [],
    "setting": "",
    "plot": "",
    "themes": [],
    "summary": ""
}}
""")
movietext = input("You : ")

# Fill the template with the user's movie description before invoking the model.
formatted_prompt = prompt.format(movie_text=movietext)

response = model.invoke(formatted_prompt)
print(response.content) 