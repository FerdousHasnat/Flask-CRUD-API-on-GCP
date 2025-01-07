from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import timedelta
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
db_path = '/tmp/users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'fallback-secret-key')  # Use environment variable for production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)

# Initialize database and JWT manager
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask CRUD API!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(f"Login attempt: username={username}, password={password}")  # Debugging log

    user = User.query.filter_by(name=username).first()
    if user:
        print(f"User found: {user.to_dict()}")  # Debugging log
    else:
        print("User not found")  # Debugging log

    if user and user.password == password:  # Replace this with hashed password logic for production
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    print(f"New user created: {new_user.to_dict()}")  # Debugging log
    return jsonify(new_user.to_dict()), 201

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    print(f"Users fetched: {[user.to_dict() for user in users]}")  # Debugging log
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    user = User.query.get_or_404(id)
    print(f"User fetched: {user.to_dict()}")  # Debugging log
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    db.session.commit()
    print(f"User updated: {user.to_dict()}")  # Debugging log
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    print(f"User deleted: {id}")  # Debugging log
    return jsonify({"message": "User deleted successfully"})

# Create database tables
if __name__ == '__main__':
    db_path = os.path.abspath('users.db')
    print(f"Database path: {db_path}")  # Log database path for debugging
    if not os.path.exists(db_path):
        print("Attempting to create database and tables...")
        with app.app_context():
            db.create_all()
        print("Database and tables created successfully!")
    else:
        print("Database already exists. Skipping creation.")

    app.run(host="0.0.0.0", port=5000, debug=True)
