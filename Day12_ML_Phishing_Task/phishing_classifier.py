from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Training data
emails = [
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediately",
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready for review",
    "Urgent: update your bank details to avoid closure",
    "Congratulations, you won a lottery, claim your reward now",
    "Meeting rescheduled to next Monday",
    "Your package delivery failed, click to reschedule",
    "Quarterly report attached for your review",
    "Your PayPal account has been limited, verify now",
]
labels = [1, 1, 0, 0, 1, 1, 0, 1, 0, 1]  # 1=phishing, 0=legit

pipe = Pipeline([
    ("vec", CountVectorizer()),
    ("clf", MultinomialNB()),
])
pipe.fit(emails, labels)

if __name__ == "__main__":
    print("\n=== Phishing Email ML Classifier ===\n")
    
    tests = [
        "Please verify your PayPal login",
        "Meeting notes from yesterday",
        "Your account will be suspended, click now",
        "Lunch plans for Friday?",
    ]
    
    for t in tests:
        pred = pipe.predict([t])[0]
        label = "PHISHING" if pred else "LEGIT"
        print(f"{label}: {t}")