import requests

# Configura tus credenciales y el endpoint de LUIS
endpoint = "https://<your-luis-endpoint>"
subscription_key = "<your-subscription-key>"
app_id = "<your-app-id>"

query = "¿Cuáles son las noticias de hoy?"

# Realiza una consulta a LUIS
url = f"{endpoint}/luis/prediction/v3.0/apps/{app_id}/slots/production/predict?subscription-key={subscription_key}&query={query}"
response = requests.get(url)
data = response.json()

# Muestra las intenciones y entidades reconocidas
print("Intenciones:", data['prediction']['topIntent'])
print("Entidades:", data['prediction']['entities'])

