from flask import Flask, render_template, request
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import time
import json
import os
from datetime import datetime


app = Flask(__name__)

# Replace 'your_key' and 'your_endpoint' with your actual key and endpoint
key = 'b4b539efb4ee4608b314b5f0d6b76dca'
endpoint = 'https://text-analytics-practice-0324.cognitiveservices.azure.com/'




def authenticate_client(key, endpoint):
    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    return client

client = authenticate_client(key, endpoint)

def analyze_sentiment(client, documents):
    response = client.analyze_sentiment(documents=documents)
    return response

def extract_key_phrases(client, documents):
    response = client.extract_key_phrases(documents=documents)
    return response

def timefmt(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

app.jinja_env.filters['timefmt'] = timefmt

@app.route('/')
def index():
    sentiment = None
    return render_template("index.html", sentiment=sentiment, current_time=time.time())

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.form['text']
    sentiment_response = analyze_sentiment(client, [text])
    sentiment = sentiment_response[0].sentiment
    scores = {
        'positive': sentiment_response[0].confidence_scores.positive,
        'neutral': sentiment_response[0].confidence_scores.neutral,
        'negative': sentiment_response[0].confidence_scores.negative
    }
    key_phrases_response = extract_key_phrases(client, [text])
    key_phrases = key_phrases_response[0].key_phrases
    save_analysis_to_history(text, sentiment, scores)
    return render_template('index.html', sentiment=sentiment, scores=scores, key_phrases=key_phrases, current_time=time.time())



@app.route('/history')
def history():
    with open('data/history.json', 'r') as history_file:
        try:
            history_data = json.load(history_file)
        except json.JSONDecodeError:
            history_data = []

    return render_template('history.html', history=history_data)

def save_analysis_to_history(text, sentiment, scores):
    with open('data/history.json', 'r') as history_file:
        try:
            history_data = json.load(history_file)
        except json.JSONDecodeError:
            history_data = []

    analysis = {
        'text': text,
        'sentiment': sentiment,
        'scores': scores,
        'timestamp': time.time()
    }
    history_data.append(analysis)

    with open('data/history.json', 'w') as history_file:
        json.dump(history_data, history_file)


if __name__ == '__main__':
    app.run(debug=True)

