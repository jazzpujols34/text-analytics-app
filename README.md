# **Text Analytics App**

This is a simple web application that uses Microsoft Azure Text Analytics API to perform sentiment analysis and extract key phrases from the text. It is built with Python, Flask, and Azure Text Analytics API. It also keeps a history of past analyses, which can be viewed on the history page.

## **Features**

- Sentiment analysis
- Key phrase extraction
- Analysis history
- Sentiment score visualization

## **Getting Started**

### **Prerequisites**

- Python 3.x
- Flask
- An Azure account with an active Text Analytics resource
- API key and endpoint for the Text Analytics resource

### **Installation**

1. Clone this repository:

```bash
git clone https://github.com/yourusername/text-analytics-app.git
cd text-analytics-app
```

1. Install required Python packages:

```python
pip install -r requirements.txt
```

1. Update **`app.py`** with your Text Analytics API key and endpoint:

```python
key = 'your_key'
endpoint = 'your_endpoint'
```

1. Run the application:

```bash
python app.py
```

The application will be accessible at **`http://127.0.0.1:5000/`**.

## **Usage**

1. Enter the text you want to analyze in the text area.
2. Click the "Analyze" button.
3. The overall sentiment, key phrases, and sentiment scores will be displayed.
4. To view the analysis history, click the "View Analysis History" button.

## **Application Structure**

- **`app.py`**: The main application file containing the Flask app, API authentication, and routing.
- **`templates/`**: Contains HTML templates for rendering the web pages.
    - **`base.html`**: The base template that includes the HTML structure and links to CSS and JS files.
    - **`index.html`**: The template for the main page with the text input form and results display.
    - **`history.html`**: The template for the history page that displays past analyses.
- **`static/`**: Contains static files such as CSS and JS.
    - **`styles.css`**: The CSS file for styling the application.
- **`data/`**: Contains the history data in JSON format.
    - **`history.json`**: Stores the history of past analyses.

## **Built With**

- **[Python](https://www.python.org/)**
- **[Flask](https://flask.palletsprojects.com/)**
- **[Microsoft Azure Text Analytics API](https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/)**
