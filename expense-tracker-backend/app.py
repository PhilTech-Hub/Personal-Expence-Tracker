from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Use MongoDB Atlas connection string
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Intelligent_tracker:Philemon.intelligent.tracker@cluster0.rampk.mongodb.net/"
)

client = MongoClient(MONGO_URI)
db = client.get_database("expense_tracker")  # Select database
# print("MongoDB connection:", client.server_info())  # Check if MongoDB is connected


@app.route("/add-expense", methods=["POST"])
def add_expense():
    data = request.json
    db.expenses.insert_one(data)
    return jsonify({"message": "Expense added successfully!"}), 201

@app.route("/get-expenses", methods=["GET"])
def get_expenses():
    expenses = list(db.expenses.find({}, {"_id": 0}))  # Exclude MongoDB ObjectId
    print("Fetched expenses:", expenses)  # Debugging statement
    return jsonify(expenses)


if __name__ == "__main__":
    app.run(debug=True)
