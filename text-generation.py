import openai

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # O usa "gpt-4" si tienes acceso
        prompt=prompt,
        max_tokens=100
    )
    print(response.choices[0].text.strip())


if __name__ == '__main__':

    openai.api_key = "<your-openai-api-key>"
    generate_text("Escribe un resumen sobre los avances en inteligencia artificial.")

