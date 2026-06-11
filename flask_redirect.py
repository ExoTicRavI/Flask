from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/old')
def old():
    return redirect(url_for('new'))

@app.route('/new')
def new():
    return "This is the new page"



if __name__ == '__main__':
    app.run(debug=True, port=5000)