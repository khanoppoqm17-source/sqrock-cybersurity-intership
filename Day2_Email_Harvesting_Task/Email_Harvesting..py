import re

def harvest_emails_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    pattern = r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}'
    emails = set(re.findall(pattern, html))
    return emails

if __name__ == "__main__":
    print("\n=== Email Harvesting (Local Test File) ===\n")
    found_emails = harvest_emails_from_file("test_page.html")
    
    if found_emails:
        print(f"Found {len(found_emails)} email(s):\n")
        for email in found_emails:
            print(f"  - {email}")
    else:
        print("No emails found.")