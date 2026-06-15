from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)

@app.route('/')
def Crud():
    students = Student.query.all()
    return render_template('Crud.html', students = students)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method =='POST':
        name1 = request.form['name']
        email1 = request.form['email']
        student = Student(name = name1, email = email1)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('Crud'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        db.session.commit()
        return redirect(url_for("Crud"))
    return render_template('edit.html')


@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("Crud"))

if __name__ == ('__main__'):
    with app.app_context():
        db.create_all()
    app.run(debug=True)