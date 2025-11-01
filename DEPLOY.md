# Project Samarth - Deployment Guide

## Quick Deploy to Streamlit Cloud

1. **Push to GitHub**:
   ```bash
   # If not already done
   git remote add origin https://github.com/yourusername/project-samarth.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository: `yourusername/project-samarth`
   - Set main file path: `app.py`
   - Add secrets in the Streamlit Cloud secrets UI:
     ```toml
     DATA_GOV_API_KEY = "your_data_gov_api_key_here"
     GEMINI_API_KEY = "your_gemini_api_key_here"  # optional
     ```

3. **Deploy**: Click "Deploy!" and your app will be live at a `https://xyz.streamlit.app` URL.

## Local Development

1. **Setup**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or: source .venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   # Windows PowerShell
   $env:DATA_GOV_API_KEY = "your_key_here"
   $env:GEMINI_API_KEY = "your_key_here"  # optional
   
   # Or create .env file (gitignored):
   echo "DATA_GOV_API_KEY=your_key_here" > .env
   echo "GEMINI_API_KEY=your_key_here" >> .env
   ```

3. **Run locally**:
   ```bash
   streamlit run app.py
   ```

## Run Tests

```bash
pytest -v
```

## Alternative Hosting

- **Heroku**: Add `Procfile` with `web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
- **Railway**: Push to GitHub, connect in Railway dashboard, set environment variables
- **Google Cloud Run**: Build Docker image, deploy to Cloud Run with environment variables

## Security Notes

- Never commit API keys to the repository
- Use platform-specific secret managers (Streamlit Secrets, Railway Variables, etc.)
- Rotate keys periodically and after any exposure
- The project `.gitignore` excludes `.env` files and virtualenvs

## Project Structure

```
project-samarth/
├── app.py                 # Main Streamlit application
├── src/                   # Core modules
│   ├── config.py          # Secret loading
│   ├── data/              # Data fetchers
│   ├── integrator.py      # Analysis layer
│   ├── llm.py            # LLM wrapper (optional)
│   └── ui/               # UI components
├── tests/                 # Test suite
├── data/raw/             # Sample data and API cache
├── docs/schema.md        # Data schema documentation
├── requirements.txt      # Python dependencies
└── .streamlit/config.toml # Streamlit configuration
```