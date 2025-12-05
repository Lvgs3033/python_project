from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage and ID counter
users = {
    1: {"username": "alice", "email": "alice@example.com"},
    2: {"username": "bob", "email": "bob@example.com"},
}
current_id = 3

# --- REST API Endpoints ---

@app.route('/users', methods=['GET'])
def get_all_users():
    """Retrieves a list of all users."""
    user_list = [{"id": uid, **data} for uid, data in users.items()]
    return jsonify(user_list)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Retrieves a specific user by ID."""
    user = users.get(user_id)
    if user:
        return jsonify({"id": user_id, **user})
    return jsonify({"message": f"User with ID {user_id} not found"}), 404

@app.route('/users', methods=['POST'])
def create_new_user():
    """Creates a new user."""
    global current_id
    data = request.get_json()

    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"message": "Invalid user data. Requires 'username' and 'email'."}), 400

    new_user = {
        "username": data['username'],
        "email": data['email']
    }
    
    users[current_id] = new_user
    response_data = {"id": current_id, **new_user}
    current_id += 1
    
    return jsonify(response_data), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_existing_user(user_id):
    """Updates an existing user's data."""
    if user_id not in users:
        return jsonify({"message": f"User with ID {user_id} not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided for update"}), 400
        
    # Update only the provided fields (username and/or email)
    user = users[user_id]
    if 'username' in data:
        user['username'] = data['username']
    if 'email' in data:
        user['email'] = data['email']
    
    return jsonify({"id": user_id, **user})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    """Deletes a user by ID."""
    if user_id in users:
        del users[user_id]
        # 204 No Content is the standard response for successful DELETE
        return '', 204
    return jsonify({"message": f"User with ID {user_id} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)