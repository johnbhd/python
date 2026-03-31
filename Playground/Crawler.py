import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def clear():
    os.system("clear")

def banner():
    print("=" * 50)
    print("     🔥 HYBRID SEO CRAWLER (PRO)")
    print("=" * 50)

def get_url():
    domain = input("👉 Domain (e.g. web.com): ").replace("http://", "").replace("https://", "").strip()

    print("\n[1] http\n[2] https")
    choice = input("👉 Select protocol: ")

    protocol = "http://" if choice == "1" else "https://"
    return protocol + domain

# 🔹 Try normal request first
def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        return res.text
    except:
        return None

# 🔹 Detect if page is empty / JS-heavy
def is_bad_html(html):
    if not html:
        return True
    return len(html.strip()) < 1000   # small content = likely JS site

# 🔹 SEO Analyzer
def analyze(html, url):
    soup = BeautifulSoup(html, "html.parser")

    print("\n📝 Title:", soup.title.string if soup.title else "None")

    desc = soup.find("meta", attrs={"name": "description"})
    print("📝 Description:", desc["content"] if desc else "None")

    print("\n📌 H1 Tags:")
    for h1 in soup.find_all("h1"):
        print("-", h1.text.strip())

    imgs = soup.find_all("img")
    missing_alt = sum(1 for img in imgs if not img.get("alt"))
    print(f"\n🖼️ Images missing alt: {missing_alt}")

    links = soup.find_all("a")
    internal = external = 0

    for link in links:
        href = link.get("href")
        if href:
            full = urljoin(url, href)
            if url in full:
                internal += 1
            else:
                external += 1

    print(f"\n🔗 Internal Links: {internal}")
    print(f"🔗 External Links: {external}")

# 🔥 MAIN
clear()
banner()

url = get_url()
print(f"\n🌐 Crawling: {url}")

html = fetch_html(url)

if is_bad_html(html):
    print("\n⚠️ Site may use JavaScript or block bots.")
    print("👉 This requires browser automation (NOT supported in Termux).")
    print("👉 Use laptop with Selenium for full crawl.")
else:
    analyze(html, url)