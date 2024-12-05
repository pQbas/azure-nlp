from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def analyze_sentiment(text):
    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    
    print(f"Sentiment: {response.sentiment}")
    print(f"Positive score: {response.confidence_scores.positive}")
    print(f"Neutral score: {response.confidence_scores.neutral}")
    print(f"Negative score: {response.confidence_scores.negative}")


if __name__ == '__main__':
    endpoint = "<your-endpoint>"
    api_key = "<your-api-key>"

    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

    analyze_sentiment("I love using Azure Cognitive Services!")

