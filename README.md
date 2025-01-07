# Secure CRUD API on Google Cloud
This project demonstrates the development, containerization, and deployment of a secure CRUD API using Python, Flask, and SQLAlchemy. The application is hosted on Google Cloud App Engine with a database managed through Google Cloud Storage. This project highlights secure user authentication with JWT (JSON Web Tokens) and containerization using Docker.

## Features
CRUD Operations: Create, Read, Update, and Delete user data.
Secure Authentication: Implemented using JWT.
Containerization: Fully containerized application using Docker.
Cloud Deployment: Deployed on Google Cloud App Engine.
Database Management: SQLite database hosted in a writable cloud environment.

## Technology Stack
Backend: Python, Flask, SQLAlchemy
Authentication: JWT (Flask-JWT-Extended)
Containerization: Docker
Cloud Platform: Google Cloud Platform (GCP)
App Engine
Cloud Storage
Database: SQLite

## Setup and Installation
Prerequisites
Python 3.12 or higher
Docker
Google Cloud SDK
A Google Cloud Platform account with billing enabled

## Local Setup
git clone https://github.com/your-username/secure-crud-api.git
cd secure-crud-api

## Install dependencies:
pip install -r requirements.txt

##Run the application locally:
python app.py
The app will be accessible at http://127.0.0.1:5000.

## Docker Setup
Build the Docker image:
docker build -t secure-crud-api .

## Run the Docker container:
docker run -p 5000:5000 secure-crud-api

## Deploy to Google Cloud

Authenticate with Google Cloud:
gcloud auth login

Set your project:
gcloud config set project <PROJECT_ID>

Deploy to App Engine:
gcloud app deploy

Access the app:
gcloud app browse

## API Endpoints
Public
POST /login: Authenticate a user and return a JWT token.
Secured (JWT Required)
POST /users: Create a new user.
GET /users: Retrieve all users.
GET /users/<id>: Retrieve a specific user by ID.
PUT /users/<id>: Update a user by ID.
DELETE /users/<id>: Delete a user by ID.

## Project Structure
secure-crud-api/
├── app.py                 # Main application code
├── requirements.txt       # Python dependencies
├── app.yaml               # Google Cloud App Engine configuration
├── Dockerfile             # Docker configuration
└── README.md              # Project documentation

## Objective
Managing secure environments using cloud-specific configurations.
Handling database configurations in read-only file systems.
Deploying containerized applications to the cloud.
Implementing secure authentication mechanisms.
