import json
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

load_dotenv()

app = Flask(__name__)

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
if not RAPIDAPI_KEY:
    raise RuntimeError(
        "RAPIDAPI_KEY environment variable is not set. "
        "Copy .env.example to .env and set your key."
    )
RAPIDAPI_HOST = "linkedin-profiles1.p.rapidapi.com"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/linkedinExtractor', methods=['POST'])
def extract_information():
    linkedinUrl = request.form['url']
    print(linkedinUrl)
    url = f"https://{RAPIDAPI_HOST}/extract"

    querystring = {"url": linkedinUrl, "html": "1"}

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if 'extractor' not in data:
        return render_template('result.html', summary_text="Error: could not extract profile data. Check the URL and try again.")
    jext = data['extractor']
    jextStr = json.dumps(jext, indent=2)
    return render_template('result.html', summary_text=jextStr)


if __name__ == '__main__':
    app.run(debug=True)