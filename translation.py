import requests
import json

def translate_text(text, target_language="es"):
    path = '/translate'
    url = f"{endpoint}{path}"
    params = {
        'api-version': '3.0',
        'to': target_language
    }
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-Type': 'application/json'
    }
    body = [{
        'text': text
    }]
    
    response = requests.post(url, params=params, headers=headers, json=body)
    translations = response.json()
    
    for translation in translations[0]['translations']:
        print(f"Traducción: {translation['text']}")


if __name__ == '__main__':

    # Configura tus credenciales
    subscription_key = "<your-subscription-key>"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "<your-region>"


    # Traduce un texto
    translate_text("Hello, how are you?", "es")

