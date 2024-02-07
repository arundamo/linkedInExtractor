import json

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/linkedinExtractor', methods=['POST'])
def extract_information():
    linkedinUrl = request.form['url']
    print(linkedinUrl)
    url = "https://linkedin-profiles1.p.rapidapi.com/extract"

    querystring = {"url": linkedinUrl, "html": "1"}

    headers = {
        "X-RapidAPI-Key": "bb153ac01emsh5fb1a35bf9c97fbp1821a9jsn952ab6de8bfa",
        "X-RapidAPI-Host": "linkedin-profiles1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    # jext = response.json()
    jext = response.json()['extractor']
    jextStr = json.dumps(jext, indent=2)
    return render_template('result.html', summary_text=jextStr)


if __name__ == '__main__':
    app.run(debug=True)