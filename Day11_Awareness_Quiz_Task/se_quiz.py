import json

QUESTIONS = [
    {"q": "An email asks you to verify your password via a link. You should:",
     "opts": ["A) Click the link", "B) Call IT directly", "C) Reply with password"],
     "ans": "B", "exp": "Always verify via official channels, never click email links."},

    {"q": "You find a USB drive in the parking lot. You should:",
     "opts": ["A) Plug it in to check", "B) Hand to security", "C) Keep it"],
     "ans": "B", "exp": "USB drops are a classic baiting attack vector."},

    {"q": "A caller claims to be IT and asks for your password. You should:",
     "opts": ["A) Give it, they're IT", "B) Ask for verification via official channel", "C) Hang up without saying anything"],
     "ans": "B", "exp": "Legitimate IT never asks for passwords over the phone."},

    {"q": "You receive an urgent email demanding immediate wire transfer. You should:",
     "opts": ["A) Process it immediately", "B) Verify via a separate known channel", "C) Ignore and delete"],
     "ans": "B", "exp": "Urgency is a common SE trigger; always verify independently."},

    {"q": "A LinkedIn message from a 'recruiter' asks for your company org chart. You should:",
     "opts": ["A) Send it to be helpful", "B) Politely decline and report if suspicious", "C) Ask a colleague to send it"],
     "ans": "B", "exp": "Attackers use pretexting on social platforms to build profiles."},

    {"q": "An SMS claims your bank account is locked and provides a link. You should:",
     "opts": ["A) Click and log in", "B) Call the bank using the number on your card", "C) Reply STOP"],
     "ans": "B", "exp": "This is smishing; always use verified contact info, not links in texts."},

    {"q": "A new employee is texted by someone claiming to be the CEO, asking for gift cards. This is:",
     "opts": ["A) Normal executive request", "B) A CEO fraud/whaling attempt", "C) A payroll process"],
     "ans": "B", "exp": "CEO fraud exploits authority and urgency to bypass scrutiny."},

    {"q": "You notice a colleague's email account sending strange links to everyone. You should:",
     "opts": ["A) Click to see what it is", "B) Report to IT/Security immediately", "C) Reply asking if it's really them"],
     "ans": "B", "exp": "The account may be compromised; report before interacting further."},

    {"q": "A website asks you to disable your antivirus to 'view content'. You should:",
     "opts": ["A) Disable it temporarily", "B) Close the site and never disable protection", "C) Ask a friend if it's safe"],
     "ans": "B", "exp": "Legitimate sites never require disabling security software."},

    {"q": "Best defense against social engineering attacks is:",
     "opts": ["A) Antivirus software alone", "B) Employee awareness and training", "C) Ignoring all emails"],
     "ans": "B", "exp": "Human awareness is the strongest defense; technology alone isn't enough."},
]

def run_quiz():
    score = 0
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\nQ{i}: {q['q']}")
        for o in q['opts']:
            print(f"   {o}")
        ans = input("Your answer (A/B/C): ").strip().upper()
        if ans == q['ans']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. {q['exp']}")
    
    print(f"\n=== Final Score: {score}/{len(QUESTIONS)} ===")
    
    report = {"score": score, "total": len(QUESTIONS)}
    with open("quiz_score.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Score saved to quiz_score.json")

if __name__ == "__main__":
    print("\n=== Social Engineering Awareness Quiz ===")
    run_quiz()