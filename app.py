from flask import Flask, render_template, request
from form import NameForm

app = Flask(__name__)
app.secret_key = "ExoTicRavi"


@app.route('/', methods =['GET','POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello,{form.name.data}!"   
    return render_template("index.html",form = form)



if __name__ == '__main__':
    app.run(debug=True, port=5000)