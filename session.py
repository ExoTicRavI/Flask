from flask import Flask, session, render_template

app = Flask(__name__)

app.secret_key = "ExoTicRavI"

@app.route("/login")
def login():
    session['username'] = 'Sashi'
    return "Logged In"

@app.route('/profile')
def profile():
    username = session.get('username')
    return f"Welcome, {username}"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return f"You have successfully logged out"

@app.route('/')
def home():
    return render_template("session.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)