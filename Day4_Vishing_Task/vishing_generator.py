def generate_vishing_script(target_company, attacker_role, pretext):
    script = f"""
=== VISHING AWARENESS SCRIPT ===
Caller Role : {attacker_role}
Target Org  : {target_company}
Pretext     : {pretext}

[OPENER]
'Hi, this is Alex from {attacker_role} at {target_company}.
We detected unusual activity on your account.'

[HOOK]
'I need to verify your identity — can you confirm
your employee ID and current password?'

[RED FLAG for Awareness]
-> Legitimate {attacker_role} will NEVER ask for passwords.
-> Always verify via official internal channels.
"""
    return script

if __name__ == "__main__":
    print("\n=== Vishing Awareness Script Generator ===\n")
    
    # Script 1: IT Support pretext
    print(generate_vishing_script("Sqrock IT", "IT Support", "Password Reset"))
    
    # Script 2: Bank pretext
    print(generate_vishing_script("National Bank", "Fraud Department", "Suspicious Transaction Alert"))
    
    # Script 3: Government pretext
    print(generate_vishing_script("Tax Authority", "Government Official", "Unpaid Tax Penalty"))