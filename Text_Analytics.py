from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Function to authenticate the Text Analytics client
def authenticate_client(key, endpoint):
    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    return client

# Replace 'my key' and 'endpoint' with your actual key and endpoint URL
key = "b4b539efb4ee4608b314b5f0d6b76dca"
endpoint = "https://text-analytics-practice-0324.cognitiveservices.azure.com/"
client = authenticate_client(key, endpoint)

# Function to perform sentiment analysis
def analyze_sentiment(client, documents):
    response = client.analyze_sentiment(documents=documents)
    return response

# List of documents to analyze
documents = [
    "Hola, buenos dias",
    "Que bien!",
    "Ayyy, que mal, espero que no sepa.",
    "Me alegro los animales.",
    "Que tonto ese tio!"
]

# Call the analyze_sentiment function
response = analyze_sentiment(client, documents)

# Process and display the results
for idx, document in enumerate(response):
    print(f"Document {idx + 1}:")
    print(f"\tOverall sentiment: {document.sentiment}")
    print("\tSentiment scores:")
    print(f"\t\tPositive: {document.confidence_scores.positive:.2f}")
    print(f"\t\tNeutral: {document.confidence_scores.neutral:.2f}")
    print(f"\t\tNegative: {document.confidence_scores.negative:.2f}")
    print()
