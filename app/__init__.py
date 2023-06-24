from flask import Flask
from pymongo import MongoClient

# Creating a Flask app instance
app = Flask(__name__)
print('Flask application initialized')

# Connecting to MongoDB
try:
    client = MongoClient('mongodb://mongodb:27017/')
    db = client['mydatabase']
    print('MongoDB connected successfully!')
except Exception as e:
    print('Error connecting to MongoDB:', e)
