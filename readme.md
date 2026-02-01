# AI Company Analyzer

An **AI-powered company analysis backend** that takes a company’s official website URL and returns:
- Structured company information
- A professional business outreach proposal  
- Cached results to avoid repeated processing  

The system is exposed as a **FastAPI service** and is designed like a real-world production backend.

---

## Overview

Given a company website URL, the system:
1. Scrapes important pages from the website
2. Extracts structured company details using AI
3. Generates a professional proposal email
4. Caches results in Firebase for faster future responses
5. Returns data via a REST API

This project focuses on **applied AI, system design, and real-world execution** rather than demos.

---

## Key Features

- Website scraping with JavaScript support (Playwright)
- AI-based structured data extraction (JSON schema enforced)
- AI-generated professional outreach proposals
- Firebase caching to reduce repeated AI calls
- FastAPI backend with CORS support
- Production-style error handling and validation

---

## API Workflow

1. Client sends a company website URL to `/analyze`
2. The system validates the URL and blocks directory websites
3. Firebase cache is checked
4. Website content is scraped and cleaned
5. AI extracts structured company data
6. AI generates a professional proposal email
7. Results are cached and returned

---

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Playwright
- BeautifulSoup
- Firebase Firestore
- python-dotenv
- Uvicorn

---

## How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
#Start FastAPI server
uvicorn app:app --reload
### Playwright Setup
Playwright requires a browser binary to render JavaScript-based websites.
Run once:
```bash
playwright install chromium
