from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)

# Database configuration
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flask_app)


# Define database models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    math_score = db.Column(db.Float, nullable=False)
    science_score = db.Column(db.Float, nullable=False)
    english_score = db.Column(db.Float, nullable=False)


# Route to submit student data
@flask_app.route('/submit', methods=['POST'])
def submit_student_data():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    # Extract student data from the form
    name = form_data.get('name')
    math_score = float(form_data.get('math_score'))
    science_score = float(form_data.get('science_score'))
    english_score = float(form_data.get('english_score'))

    # Save the student data to the database
    student = Student(name=name, math_score=math_score, science_score=science_score, english_score=english_score)
    db.session.add(student)
    db.session.commit()

    print("Student data submitted successfully")
    return redirect('/')


# Route to display student data
@flask_app.route('/students', methods=['GET'])
def view_students():
    students = Student.query.all()
    return render_template('students.html', students=students)


# Route for adding new student data
@flask_app.route('/add_data', methods=['GET'])
def add_data():
    return render_template('add_data.html')


# Route for calculating and displaying performance
@flask_app.route('/performance', methods=['GET'])
def performance():
    students = Student.query.all()
    performance_data = []

    for student in students:
        average_score = (student.math_score + student.science_score + student.english_score) / 3
        performance = 'Excellent' if average_score >= 90 else 'Good' if average_score >= 75 else 'Needs Improvement'
        performance_data.append({
            'name': student.name,
            'average_score': average_score,
            'performance': performance
        })

    return render_template('performance.html', performance_data=performance_data)


# Initialize database
with flask_app.app_context():
    db.create_all()

if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )
