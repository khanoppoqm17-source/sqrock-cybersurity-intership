from flask import Flask, request

app = Flask(__name__)

# Fake credentials for lab testing only
VALID_USER = "admin"
VALID_PASS = "letmein"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == VALID_USER and password == VALID_PASS:
        return "Welcome admin!", 200
    else:
        return "Invalid credentials", 401

if __name__ == "__main__":
    app.run(port=5000)