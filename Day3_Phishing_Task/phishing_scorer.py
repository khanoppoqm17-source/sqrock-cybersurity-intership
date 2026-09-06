import re
from urllib.parse import urlparse

KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]

def phish_score(url):
    p = urlparse(url)
    score = 0
    
    if not url.startswith("https"):
        score += 30
    
    for kw in KEYWORDS:
        if kw in p.netloc:
            score += 20
    
    if p.netloc.count('.') > 3:
        score += 25
    
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', p.netloc):
        score += 40
    
    return min(score, 100)

if __name__ == "__main__":
    urls = [
        "https://paypal-login.evil.com/verify",
        "https://github.com",
        "http://192.168.1.1/bank-login",
        "https://secure-update-account.suspicious-site.co.xyz.com"
    ]
    
    print("\n=== Phishing URL Risk Scorer ===\n")
    for u in urls:
        print(f"{u} -> Risk: {phish_score(u)}%")