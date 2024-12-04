from utils.db import db

# Parent table: Student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentName = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    # Relationship to Exam
    exams = db.relationship('Exam', backref='student', lazy=True)

# Child table: Exam
class Exam(db.Model):
    exam_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    exam_date = db.Column(db.String(100), nullable=False)
    remarks = db.Column(db.String(255), nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

# Login table for teachers/admins
class Login(db.Model):
    login_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)