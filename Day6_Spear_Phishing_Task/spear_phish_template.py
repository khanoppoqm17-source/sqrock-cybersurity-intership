def spear_phish_template(target):
    return f"""
From    : it-support@{target['company'].lower()}.com
To      : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}.
Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal/awareness-test

Regards,
IT Security Team
"""

if __name__ == "__main__":
    print("\n=== Spear Phishing Awareness Training Templates ===\n")
    
    targets = [
        {"name": "Riya Sharma", "email": "riya@company.com",
         "company": "Sqrock", "location": "Bangalore, India"},
        
        {"name": "Ahmed Khan", "email": "ahmed@techcorp.com",
         "company": "TechCorp", "location": "Karachi, Pakistan"},
        
        {"name": "Sarah Lee", "email": "sarah@globalbank.com",
         "company": "GlobalBank", "location": "Singapore"}
    ]
    
    for t in targets:
        print(spear_phish_template(t))
        print("-" * 50)