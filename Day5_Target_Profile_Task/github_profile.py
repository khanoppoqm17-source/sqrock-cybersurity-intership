import requests
import json

def github_profile(username):
    base = "https://api.github.com"
    
    try:
        u = requests.get(f"{base}/users/{username}", timeout=10).json()
        repos = requests.get(f"{base}/users/{username}/repos", timeout=10).json()
        
        langs = {}
        for r in repos[:10]:
            if isinstance(r, dict) and r.get('language'):
                langs[r['language']] = langs.get(r['language'], 0) + 1
        
        profile = {
            "name": u.get("name"),
            "company": u.get("company"),
            "location": u.get("location"),
            "public_repos": u.get("public_repos"),
            "top_langs": langs,
            "bio": u.get("bio"),
        }
        
        print(json.dumps(profile, indent=2))
        return profile
    
    except Exception as e:
        print(f"[!] Error fetching profile: {e}")
        return None

if __name__ == "__main__":
    print("\n=== GitHub OSINT Target Profile ===\n")
    github_profile("torvalds")