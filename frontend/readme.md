🚀 AI Company Analyzer

An AI-powered web application that analyzes a company’s official website, extracts structured business information, and generates a professional outreach proposal automatically.

This project combines web scraping, AI-driven structured extraction, proposal generation, caching with Firebase, and a clean frontend UI.

📌 Problem Statement

Manually researching companies and preparing outreach proposals is:

Time-consuming

Repetitive

Error-prone

Difficult to scale

This project automates the entire process using AI and web scraping by taking just a company website URL as input.

🎯 Key Features

🔗 Single URL Input – User provides only the company website link

🌐 Multi-page Website Scraping – Automatically scrapes important pages (About, Services, Products, Contact, etc.)

🧠 AI-Based Structured Data Extraction – Converts raw website text into a strict JSON schema

✉️ AI Proposal Generation – Generates a professional outreach email based on extracted data

🔥 Firebase Caching – Avoids repeated scraping and AI calls for the same company

🛑 Directory Website Blocking – Prevents scraping listing/review websites (Clutch, GoodFirms, etc.)

🎨 Clean Frontend UI – Card-based layout with readable paragraphs and email-style proposal

⏱ Performance Logging – Measures scraping, extraction, and proposal generation time

🏗️ Tech Stack
Backend

FastAPI – API framework

Playwright – Dynamic multi-page web scraping

BeautifulSoup – HTML text extraction and cleanup

OpenAI API – AI-powered extraction and proposal generation

Firebase Firestore – Caching and storage

Frontend

HTML

CSS

Vanilla JavaScript (Fetch API)

📁 Project Structure
company_ai_analyzer/
│
├── app.py                     # Main FastAPI application
├── smart_scraper.py           # Multi-page website scraper
├── extractor.py               # AI-based company info extraction (JSON Schema)
├── proposal_generator.py      # AI-based proposal generation (JSON Schema)
├── firebase_db.py              # Firebase Firestore operations
├── utils.py                   # Helper utilities (domain extraction, etc.)
│
├── frontend/
│   ├── index.html              # Frontend UI
│   ├── style.css               # UI styling
│   └── script.js               # Frontend logic & API calls
│
├── .env                        # Environment variables (API keys)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

🔁 Application Flow (End-to-End)

User enters a company website URL in the frontend UI

Frontend sends request to /analyze API

Backend:

Extracts domain

Blocks directory/listing websites

Checks Firebase cache

If not cached:

Scrapes multiple important website pages

Cleans and aggregates visible text

AI extracts structured company data using a strict JSON schema

AI generates a professional outreach proposal

Result is saved to Firebase

Structured response is returned to frontend and displayed in a clean UI

🧠 AI Output Structure
Company Profile (Schema-based)

Company Name

About Company

Services

Projects / Products

Industries

Technologies

Team / Employees

Contact Details

Proposal Output

Email Subject

Professional Email Body

Both outputs strictly follow predefined JSON Schemas for reliability and consistency.

🛡️ Why JSON Schema Was Used

Ensures predictable output

Prevents missing or extra fields

Makes data safe for storage (Firebase)

Improves frontend rendering

Reduces AI hallucination issues

⚙️ How to Run the Project
1️⃣ Backend Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Create a .env file:

OPENAI_API_KEY=your_openai_api_key
FIREBASE_CREDENTIALS_PATH=path_to_firebase_key.json


Run backend:

uvicorn app:app --reload


Open:

http://127.0.0.1:8000/docs

2️⃣ Frontend Setup

Option 1 (Simple):

Open frontend/index.html directly in browser

Option 2 (Recommended):

Use VS Code Live Server

Right-click → Open with Live Server

🌍 CORS Support

CORS middleware is enabled to allow frontend and backend communication during development.

🚧 Known Limitations

Initial scraping can take time for large websites

Dynamic sites with heavy animations may delay scraping

Proposal tone may need fine-tuning for specific industries

🔮 Future Enhancements

React-based frontend

Proposal download (PDF / Email)

Company comparison

User authentication

Analytics dashboard

Deployment on cloud (AWS / GCP / Vercel)