# Project Samarth — Agri-Climate Q&A Prototype

This repository contains a minimal prototype for the Project Samarth challenge: an end-to-end (data -> reasoning -> chat UI) scaffold that uses data.gov.in resources and optionally a Gemini LLM to answer questions about agriculture and climate in India.

What is included
- `app.py` — Streamlit-based chat UI and tool functions to fetch agriculture & climate resources from data.gov.in. Reads keys from environment.
- `data_ingest.py` — small CLI to fetch a resource, save raw JSON, and write a basic SQLite table.
- `requirements.txt` — Python dependencies.
- `.env.example` — example environment variables.

Quickstart
1. Create and activate a Python environment (3.10+ recommended).
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your `DATA_GOV_API_KEY` and optionally `GEMINI_API_KEY`.

4. Run the Streamlit app:

```powershell
streamlit run app.py
```

5. Use `data_ingest.py` to fetch a dataset and save it locally:

```powershell
python data_ingest.py --resource 35be999b-0208-4354-b557-f6ca9a5355de --state Karnataka --district "Bengaluru Urban" --year 2020
```

Security notes
- Do not commit your API keys to source control. Use environment variables or a secrets manager.

Secrets / API keys
-------------------
Prefer providing API keys via Streamlit `secrets` when deploying the app (this keeps secrets out of your repo). Locally you can use a `.env` file or plain environment variables. The app will look for keys in Streamlit `secrets` first, then fall back to environment variables (and values loaded via `.env`).

Example `~/.streamlit/secrets.toml` (or a `.streamlit/secrets.toml` in your project when deploying):

```toml
# ~/.streamlit/secrets.toml
# Use placeholders here. Do NOT store real keys in the repo.
DATA_GOV_API_KEY = "YOUR_DATA_GOV_API_KEY"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  # optional
```

Example `.env` (for local development, the repo already includes `python-dotenv` support):

```text
DATA_GOV_API_KEY=YOUR_DATA_GOV_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Quick local PowerShell example (one-liner) to run with an env var set for the session:

```powershell
$env:DATA_GOV_API_KEY = 'YOUR_DATA_GOV_API_KEY'; streamlit run app.py
```
Next steps (suggested)
- Implement robust schema mapping for agriculture datasets (map column names to canonical names).
- Add multi-source joins (state/district normalization) between agricultural and climate tables.
- Implement richer question parsing and a controlled chaining interface to call tools programmatically from the LLM responses.
 
Architecture & next steps
------------------------
This repo has been refactored into a small package under `src/`:

- `src/config.py` — secret loading and data directory setup
- `src/data/*` — fetchers for agriculture and climate datasets
- `src/integrator.py` — analysis helpers (aggregates, top-crops, simple trends)
- `src/llm.py` — Gemini wrapper (optional)
- `src/ui/app.py` — Streamlit frontend (rule-based router fallback)

Developer quick-start (local)
1. Install dependencies into your Python environment (PowerShell):

```powershell
# (optional) activate your virtualenv
.\samarth.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

2. Run the Streamlit app (example):

```powershell
streamlit run src/ui/app.py
```

Loom script (2 minutes)
- 0:00-0:10 — Title and quick overview of what you'll show
- 0:10-0:40 — datasets chosen (resource IDs) and schema mapping mention
- 0:40-1:20 — demo one question end-to-end (ask -> fetch -> analyze -> cite)
- 1:20-1:50 — architecture choices and security notes (secrets + history cleanup)
- 1:50-2:00 — link to repo and how to run the demo

