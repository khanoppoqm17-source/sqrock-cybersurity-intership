def fake_profile_score(profile):
    score = 0
    
    age_days = profile.get("account_age_days", 365)
    if age_days < 30:
        score += 30
    
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)
    ratio = following / max(followers, 1)
    if ratio > 10:
        score += 25
    
    if profile.get("no_profile_pic"):
        score += 20
    
    if profile.get("posts", 100) < 5:
        score += 15
    
    if profile.get("default_bio"):
        score += 10
    
    return min(score, 100)

if __name__ == "__main__":
    print("\n=== Fake/Bot Profile Detector ===\n")
    
    profiles = [
        {"account_age_days": 7, "followers": 2, "following": 900,
         "no_profile_pic": True, "posts": 1, "default_bio": True},
        
        {"account_age_days": 1200, "followers": 4500, "following": 320,
         "no_profile_pic": False, "posts": 870, "default_bio": False},
        
        {"account_age_days": 45, "followers": 50, "following": 600,
         "no_profile_pic": True, "posts": 3, "default_bio": False},
        
        {"account_age_days": 800, "followers": 1200, "following": 400,
         "no_profile_pic": False, "posts": 250, "default_bio": False},
        
        {"account_age_days": 15, "followers": 10, "following": 500,
         "no_profile_pic": True, "posts": 0, "default_bio": True},
    ]
    
    for i, p in enumerate(profiles, 1):
        score = fake_profile_score(p)
        verdict = "LIKELY FAKE" if score >= 50 else "LIKELY REAL"
        print(f"Profile {i} -> Fake Score: {score}% ({verdict})")