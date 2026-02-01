from urllib.parse import urlparse, urljoin

def get_domain(url):
    return urlparse(url).netloc

def get_internal_links(base_url, soup):
    links = set()
    base_domain = urlparse(base_url).netloc

    for a in soup.find_all("a", href=True):
        full_url = urljoin(base_url, a["href"])
        if urlparse(full_url).netloc == base_domain:
            links.add(full_url)

    return list(links)
