from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def analyze_sentiment(texts):
    print('> analyze sentiment ...')
    response = client.analyze_sentiment(documents=texts)
    
    for document in response:
        print(f"Sentiment: {document.sentiment}")
        print(f"Positive score: {document.confidence_scores.positive}")
        print(f"Neutral score: {document.confidence_scores.neutral}")
        print(f"Negative score: {document.confidence_scores.negative}")
        print("-----")

def extract_key_phrases(texts):
    print('> extracting key phrases ...')
    response = client.extract_key_phrases(documents=texts)
    
    for document in response:
        print(f"Key phrases: {document.key_phrases}")
        print("-----")


def detect_language(texts):
    print('> detecting language ...')
    response = client.detect_language(documents=texts)
    
    for document in response:
        print(f"Detected language: {document.primary_language.name}")
        print(f"Language confidence score: {document.primary_language.confidence_score}")
        print("-----")


if __name__ == '__main__':
    endpoint = 'replace with your endpoint service'
    api_key = 'replace with your api-key' 

    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

    texts = [
        "I love using Azure Cognitive Services. It's fantastic!",
        "The weather is nice today."
    ]

    analyze_sentiment(texts)
    extract_key_phrases(texts)
    detect_language(texts)

