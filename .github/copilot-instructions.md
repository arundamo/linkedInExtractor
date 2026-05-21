# Copilot Instructions — LinkedIn Extractor

## Project Purpose

This is a **Flask web application** that extracts structured profile data from public LinkedIn URLs via the [linkedin-profiles1 RapidAPI](https://rapidapi.com/mgujjargamingm/api/linkedin-profiles1). The extracted data is returned as formatted JSON.

---

## Architecture

| File | Role |
|------|------|
| `app.py` | Flask entry point; defines the `/` and `/linkedinExtractor` routes |
| `templates/index.html` | Form page — accepts a LinkedIn URL |
| `templates/result.html` | Result page — renders the extracted JSON |
| `requirements.txt` | Python dependencies |
| `.env.example` | Template for required environment variables |

---

## Key Conventions

- **No hardcoded secrets.** The RapidAPI key is read from the `RAPIDAPI_KEY` environment variable.
- **Single external dependency:** all profile data comes from `https://linkedin-profiles1.p.rapidapi.com/extract`.
- **Minimal templating:** HTML templates use Jinja2 and live in `templates/`.
- **Form POST for the web UI;** to expose a machine-readable interface, add a `/api/extract` route that accepts JSON and returns JSON.

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `RAPIDAPI_KEY` | RapidAPI key with access to `linkedin-profiles1` |

Copy `.env.example` to `.env` and fill in the value before running locally.

---

## Running Locally

```bash
pip install -r requirements.txt
cp .env.example .env  # then edit .env
flask run
```

---

## Adding New Features

- **New routes** go in `app.py`.
- **New templates** go in `templates/`.
- **New dependencies** must be added to `requirements.txt`.
- Always load secrets from environment variables — never hard-code credentials.

---

## Agent-Callable Endpoint

`POST /linkedinExtractor` accepts `application/x-www-form-urlencoded` with a single `url` field and returns an HTML page containing the JSON profile. To use this endpoint programmatically, parse the `<p>` tag content, or extend the app with a `/api/extract` JSON endpoint (see README for an example).
