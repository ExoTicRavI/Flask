from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sashilal120@gmail.com'
app.config['MAIL_PASSWORD'] = 'uady wtet yxkv mgqg'
app.config['MAIL_DEFAULT_SENDER'] = 'sashilal120@gmail.com'

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    info = None

    if request.method == 'POST':
        raw_emails = request.form.get('emails', '')
        body = request.form.get('message', '')
        email = [email.strip() for email in raw_emails.split(',') if email.strip()]

        msg = Message("New Notification", recipients=email)
        msg.body = body
        mail.send(msg)
        
        info = {"status": "success", "text": "Sent successfully!"}

    return render_template('send_email.html', info=info)

if __name__ == '__main__':
    app.run(debug=True, port=5000)