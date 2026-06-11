from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/setcookie')
def set_cookie():
    resp = make_response("Cookies has been set")
    resp.set_cookie('username', 'Sashi', max_age=3600)
    return resp

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username')
    return f"hello {username}"

@app.route('/delcookie')
def del_cookie():
    resp = make_response("Cookies has been deleted")
    resp.set_cookie('username', '', expires=0)
    return resp

@app.route('/delcookie1')
def del_cookie1():
    resp = make_response("Cookies has been deleted")
    resp.delete_cookie('username')
    return resp

@app.route('/')
def home():
    return render_template('cookies.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

