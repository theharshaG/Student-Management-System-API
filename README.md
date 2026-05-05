# Student-Management-System-API

Student Management System API (Flask + SQLite)
## Overview

This project is a backend-based Student Management System built using Flask and SQLite. It provides RESTful APIs to perform CRUD (Create, Read, Update, Delete) operations on student records.

The system allows adding, viewing, updating, deleting, searching, and filtering student data, making it a simple yet powerful backend project for learning web development and database integration.

## Features
Add new student records
View all students
Update student details
Delete student records
Search students by name
Filter students by age
Count total number of students
SQLite database integration
REST API design

## Technologies Used
Python
Flask
Flask SQLAlchemy
SQLite
REST API

## Project Structure
student-management-api/
│
├── app.py
├── students.db
├── templates/
│   └── index.html
└── README.md

## How to Run
1. Install Dependencies
pip install flask flask_sqlalchemy
2. Run Application
python app.py

Server will start at:

http://127.0.0.1:5000
3. Open Browser
http://127.0.0.1:5000

## How It Works
Flask handles API requests
SQLAlchemy manages database operations
SQLite stores student records
API endpoints perform CRUD operations
Data is returned in JSON format

## API Endpoints
Add Student

POST /add

{
  "name": "Harsha",
  "age": 21
}
Get All Students

GET /students

Update Student

PUT /update/<id>

{
  "name": "Updated Name",
  "age": 22
}
Delete Student

DELETE /delete/<id>

Search by Name

GET /search?name=Har

Filter by Age

GET /filter?age=21

Count Students

GET /count

Database
SQLite database file: students.db
Table: Student
Fields:
id (Primary Key)
name (String)
age (Integer)
Circuit Diagram

Not applicable for this project.

## Output

You can test APIs using:

Postman
Browser (for GET requests)
Curl

## Future Improvements
Add frontend dashboard
Add authentication (JWT)
Pagination support
Input validation
Error handling improvements
Deploy to cloud (Render / Railway)

## Author
Harsha G
Learning Python | Embedded Systems | IoT
