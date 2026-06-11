from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)

@app.route('/add')
def addstudent():
    Student = student(name = 'Sashi kumar lal', email = 'sashilal120@gmail.com')
    db.session.add(Student)
    db.session.commit()
    return "Student added to our database!"

@app.route('/students')
def list_students():
    Students = student.query.all()
    return '<br>'.join([f"{s.id}. {s.name} - {s.email}" for s in Students])


@app.route('/')
def home():
    return render_template("db.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)