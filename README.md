# LinkedIn Extractor

A lightweight Flask web application that extracts structured profile data from any public LinkedIn URL using the [linkedin-profiles1 RapidAPI](https://rapidapi.com/mgujjargamingm/api/linkedin-profiles1).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [AI Agent Usage](#ai-agent-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

LinkedIn Extractor lets you paste any public LinkedIn profile URL into a simple web form and instantly retrieves a structured JSON summary of that profile — name, headline, experience, education, skills, and more.

The backend calls the [linkedin-profiles1 RapidAPI](https://rapidapi.com/mgujjargamingm/api/linkedin-profiles1), formats the response, and renders it in the browser.

---

## Features

- 🔍 **One-click extraction** — paste a URL, click Extract, see results.
- 📄 **JSON output** — clean, indented JSON ready to parse or forward to downstream tools.
- 🔑 **Secrets-safe** — API key loaded from environment variables; never hard-coded.
- 🐍 **Minimal stack** — Flask + Requests; no database required.
- 🤖 **AI-agent ready** — exposes a REST endpoint that any LLM agent or automation tool can call directly.

---

## Project Structure

```
linkedInExtractor/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── .env.example           # Template for required environment variables
├── templates/
│   ├── index.html         # Home page — URL input form
│   └── result.html        # Result page — extracted JSON display
└── .github/
    └── copilot-instructions.md  # AI agent / Copilot context
```

---

## Prerequisites

| Tool | Minimum version |
|------|----------------|
| Python | 3.9+ |
| pip | 23+ |
| A RapidAPI account with access to **linkedin-profiles1** | — |

---

## Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/arundamo/linkedInExtractor.git
cd linkedInExtractor

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Open .env and set RAPIDAPI_KEY to your key
```

---

## Configuration

The application reads the following environment variables at startup:

| Variable | Required | Description |
|----------|----------|-------------|
| `RAPIDAPI_KEY` | ✅ Yes | Your RapidAPI key for the linkedin-profiles1 API |

**Obtaining a RapidAPI key:**

1. Create a free account at [rapidapi.com](https://rapidapi.com).
2. Subscribe to the [linkedin-profiles1 API](https://rapidapi.com/mgujjargamingm/api/linkedin-profiles1).
3. Copy your key from the API's "Code Snippets" panel.
4. Paste it as `RAPIDAPI_KEY` in your `.env` file.

> **Tip:** Install `python-dotenv` (already in `requirements.txt`) so the app loads `.env` automatically in development.

---

## Running the Application

```bash
# Development server (auto-reload)
flask run

# Or directly via Python
python app.py
```

Open your browser at `http://127.0.0.1:5000`.

---

## API Reference

### `POST /linkedinExtractor`

Extracts profile data for a given LinkedIn URL.

**Request (form-encoded)**

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Full public LinkedIn profile URL |

**Example with curl:**

```bash
curl -X POST http://127.0.0.1:5000/linkedinExtractor \
     -d "url=https://www.linkedin.com/in/example-profile"
```

**Response**

Returns an HTML page containing the extracted profile as a pretty-printed JSON string. The JSON schema mirrors the `extractor` object returned by the RapidAPI endpoint and typically includes:

```json
{
  "name": "Jane Doe",
  "headline": "Senior Software Engineer",
  "location": "San Francisco, CA",
  "summary": "...",
  "experience": [...],
  "education": [...],
  "skills": [...]
}
```

---

## AI Agent Usage

This application is designed to be callable by LLM-based agents and automation workflows.

### Using the REST endpoint from an agent

Any agent that can make HTTP requests can call the `/linkedinExtractor` endpoint directly:

```python
import requests

response = requests.post(
    "http://localhost:5000/linkedinExtractor",
    data={"url": "https://www.linkedin.com/in/example-profile"}
)
# Parse the HTML response or extend the endpoint to return JSON
print(response.text)
```

### Extending the endpoint for pure JSON output

To make the endpoint more agent-friendly, you can add a `/api/extract` route that returns `application/json`:

```python
from flask import jsonify

@app.route('/api/extract', methods=['POST'])
def extract_api():
    linkedin_url = request.json.get('url')
    # ... same extraction logic ...
    return jsonify(jext)
```

### GitHub Copilot

This repository includes `.github/copilot-instructions.md` with context about the codebase, making GitHub Copilot and Copilot agents aware of the project's conventions and architecture.

---

## Contributing

1. Fork the repository and create a feature branch.
2. Make your changes and ensure `flask run` still works.
3. Open a pull request with a clear description of your changes.

---

## License

This project is provided as-is for educational and personal use. See [LICENSE](LICENSE) for details.
