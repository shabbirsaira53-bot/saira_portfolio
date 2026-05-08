from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")
        
        # Username 'sara' aur password '123' rakha hai
        if user == "sara" and pwd == "123":
            return "<h2>Success! You are logged in.</h2><a href='/'>Go back to Portfolio</a>"
        else:
            return "<h2>Invalid Password! Please try again.</h2><a href='/login'>Try Again</a>"
            
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)