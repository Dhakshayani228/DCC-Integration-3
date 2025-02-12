from flask import Flask, request, jsonify
import os
import sqlite3

app = Flask(__name__)

# --- Define Absolute Path for the Database ---
BASE_DIR = os.path.dirname(os.path.abspath("C:\\Users\\Ramya\\Downloads\\Projetcs\\DCC Integration\\FlaskServer.py"))  # Get current script directory
DB_PATH = os.path.join(BASE_DIR, "database")  # Database folder inside project
DB_FILE = os.path.join(DB_PATH, "inventory.db")  # Full path to database file

# Ensure database directory exists
if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

# --- Database Setup ---
def init_db():
    try:
        conn = sqlite3.connect(DB_FILE)  # Use absolute path
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS inventory (name TEXT PRIMARY KEY, quantity INTEGER)")
        conn.commit()
        conn.close()
        print(f"Database initialized at: {DB_FILE}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

init_db()

# --- API Endpoints ---
@app.route('/')
def home():
    return "Flask Server is Running. Use API endpoints to interact."

# Existing /file-path route
@app.route('/file-path', methods=['GET'])
def file_path():
    project_path = request.args.get('projectpath', 'false') == 'true'
    return jsonify({"path": "/path/to/file.ma" if not project_path else "/path/to/project"})

@app.route('/transform', methods=['POST'])
def transform():
    data = request.json
    print(f"Received transform data: {data}")

    # Extract transformation parameters
    object_name = data.get("object", "Cube")
    position = data.get("position", [0, 0, 0])
    rotation = data.get("rotation", [0, 0, 0])  # Default rotation
    scale = data.get("scale", [1, 1, 1])  # Default scale

    return jsonify({
        "message": "Transform received",
        "data": {
            "object": object_name,
            "position": position,
            "rotation": rotation,
            "scale": scale
        }
    }), 200


@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.json
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (data['name'], data['quantity']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Item added"})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route('/update-quantity', methods=['PUT'])
def update_quantity():
    data = request.json
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("UPDATE inventory SET quantity=? WHERE name=?", (data['new_quantity'], data['name']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Quantity updated"})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
