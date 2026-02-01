from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

IMPORTANT_KEYWORDS = [
    "about",
    "company",
    "services",
    "solutions",
    "products",
    "portfolio",
    "industries",
    "contact",
    "careers"
]

def extract_visible_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    return soup.get_text(separator=" ", strip=True)

def get_important_links(base_url, page):
    links = set()
    domain = urlparse(base_url).netloc

    anchors = page.query_selector_all("a[href]")
    for a in anchors:
        href = a.get_attribute("href")
        if not href:
            continue

        href_lower = href.lower()
        if any(key in href_lower for key in IMPORTANT_KEYWORDS):
            full_url = urljoin(base_url, href)
            if urlparse(full_url).netloc == domain:
                links.add(full_url)

    return list(links)

def scrape_company_website(url: str, max_pages=8) -> str:
    collected_text = ""
    visited = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        page.wait_for_timeout(2000)

        collected_text += extract_visible_text(page.content())

        important_links = get_important_links(url, page)

        for link in important_links[:max_pages]:
            if link in visited:
                continue
            visited.add(link)

            try:
                page.goto(link, wait_until="domcontentloaded", timeout=15000)
                page.wait_for_timeout(2000)

                collected_text += " " + extract_visible_text(page.content())
                
            except Exception as e:
                print(f"[SCRAPER] Skipped {link}: {e}")
                continue

        browser.close()

    return collected_text[:30000]
