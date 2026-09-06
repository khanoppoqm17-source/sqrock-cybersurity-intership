import re
import json
import datetime
from urllib.parse import urlparse

# ---------- Module 1: OSINT (simplified) ----------
def run_osint(domain):
    print(f"\n[OSINT] Simulated passive recon on: {domain}")
    print(f"[OSINT] Registrar, DNS, and geolocation would be gathered here.")

# ---------- Module 2: Target Profile ----------
def build_profile():
    profile = {
        "name": "Riya Sharma",
        "company": "Sqrock",
        "location": "Bangalore, India"
    }
    print(f"\n[PROFILE] Target profile built:\n{json.dumps(profile, indent=2)}")
    return profile

# ---------- Module 3: Phishing URL Scorer ----------
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

def run_phish_check(url):
    score = phish_score(url)
    print(f"\n[PHISH SCORER] {url} -> Risk: {score}%")

# ---------- Module 4: Spear Phishing Template ----------
def spear_phish_template(target):
    return f"""
From    : it-support@{target['company'].lower()}.com
To      : {target['name'].lower().replace(' ', '.')}@{target['company'].lower()}.com
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}.
Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal/awareness-test

Regards,
IT Security Team
"""

def run_template(target):
    print(f"\n[TEMPLATE] Generated spear-phishing awareness email:")
    print(spear_phish_template(target))

# ---------- Module 5: Incident Response ----------
def ir_response(incident):
    print(f"\n[IR] Incident Response Triggered")
    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")
    
    actions = []
    if incident['severity'] in ('HIGH', 'CRITICAL'):
        actions += ["LOCK user account", "Revoke active sessions", "Notify SOC team"]
    if incident['type'] == 'phishing':
        actions += ["Quarantine email", "Block sender domain"]
    
    print("Actions Taken:")
    for a in actions:
        print(f"   [x] {a}")
    
    report = {"incident": incident, "actions": actions, "timestamp": str(datetime.datetime.now())}
    with open("ir_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("IR report saved: ir_report.json")

# ---------- Main Menu ----------
MODULES = {
    "osint": "Run passive OSINT on a domain",
    "profile": "Build target profile from public data",
    "phish": "Score a URL for phishing indicators",
    "template": "Generate spear-phishing training email",
    "ir": "Trigger incident response workflow",
    "exit": "Exit the simulator"
}

def menu():
    while True:
        print("\n" + "="*45)
        print("     SE ATTACK CHAIN SIMULATOR")
        print("     Sqrock Cybersecurity Internship")
        print("="*45)
        for k, v in MODULES.items():
            print(f"  [{k}] {v}")
        
        choice = input("\nSelect module: ").strip().lower()
        
        if choice == "osint":
            run_osint("example.com")
        elif choice == "profile":
            build_profile()
        elif choice == "phish":
            run_phish_check("https://paypal-login.evil.com/verify")
        elif choice == "template":
            target = {"name": "Riya Sharma", "company": "Sqrock", "location": "Bangalore, India"}
            run_template(target)
        elif choice == "ir":
            ir_response({"type": "phishing", "severity": "HIGH", "user": "riya@sqrock.com"})
        elif choice == "exit":
            print("\nExiting simulator. Stay safe!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()