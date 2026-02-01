from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from smart_scraper import scrape_company_website
from extractor import extract_company_info
from firebase_db import save_company_data, get_company_data
from proposal_generator import generate_proposal
from utils import get_domain
import traceback
import time   # ✅ ADDED FOR TIMING

app = FastAPI(title="AI Company Analyzer")   # ✅ APP CREATED

#  ADD CORS IMMEDIATELY AFTER APP CREATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
#  Directory / Listing websites (not official company sites)
BLOCKED_DOMAINS = [
    "techbehemoths.com",
    "clutch.co",
    "goodfirms.co",
    "g2.com",
    "trustpilot.com"
]

CACHE_VERSION = "v2"

@app.get("/")
def home():
    return {
        "message": "AI Company Analyzer API is running",
        "usage": "Go to /docs to analyze a company website"
    }

@app.post("/analyze")
def analyze_company(
    url: str = Query(..., description="Company website URL")
):
    try:
        # 🔹 Extract domain
        domain = get_domain(url)
        if not domain:
            return {"error": "Invalid URL provided"}

        # 🔹 Build versioned cache key
        cache_key = f"{CACHE_VERSION}:{domain}"

        # 🔹 Block directory websites
        if any(domain.endswith(d) for d in BLOCKED_DOMAINS):
            return {
                "error": "Directory website detected",
                "message": "Please provide the official company website URL, not a listing or review page."     
            }

        # 🔹 Check Firebase cache
        cached = get_company_data(cache_key)
        if cached:
            return {
                "source": "firebase",
                "data": cached
            }

        # 🔹 Scrape website (TIMED)
        start = time.time()
        text = scrape_company_website(url)
        scrape_time = time.time() - start
        print(f"[DEBUG] Scraping time: {scrape_time:.2f}s")

        if not text:
            return {"error": "Failed to scrape website content"}

        # 🔹 AI extraction (TIMED)
        start = time.time()
        company_profile = extract_company_info(text)
        extract_time = time.time() - start
        print(f"[DEBUG] Extraction time: {extract_time:.2f}s")

        # 🔹 AI proposal generation (TIMED)
        start = time.time()
        proposal = generate_proposal(company_profile)
        proposal_time = time.time() - start
        print(f"[DEBUG] Proposal time: {proposal_time:.2f}s")

        # 🔹 Final structured result
        result = {
            "url": url,
            "company_profile": company_profile,
            "proposal": proposal
        }

        # 🔹 Save to Firebase
        save_company_data(cache_key, result)

        return {
            "source": "fresh",
            "data": result
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "error": "Internal server error",
            "details": str(e)
        }
