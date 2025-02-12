DCC Integration

📌 Project Description

This project integrates a Flask server with Blender to apply transformations (position, rotation, scale) to 3D objects dynamically. It allows real-time updates using API endpoints and synchronizes with Blender via Python scripts.

🚀 Features

Flask server for handling transformation data

API endpoint for sending object transformations

Blender script to fetch and apply transformations

Supports position, rotation, and scale changes

Uses bpy.app.timers.register() for periodic updates

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Dhakshayani228/DCC-Integration-3.git
cd DCC-Integration-3

2️⃣ Install Dependencies

Make sure you have Python installed, then install Flask and requests:

pip install flask requests

3️⃣ Run the Flask Server

python flask_server.py

It should show: Flask Server is Running. Use API endpoints to interact.

4️⃣ Run the Blender Script

Open Blender

Open Scripting tab → New script

Load fetch_transform.py

Run the script

📡 API Endpoints

Method

Endpoint

Description

GET

/

Checks if the Flask server is running

POST

/transform

Sends object transformation data

Example API Request:

curl -X POST "http://127.0.0.1:8000/transform" -H "Content-Type: application/json" -d '{ "object": "cube", "position": [1, 2, 3], "rotation": [45, 90, 0] }'

🛠️ Technologies Used

Flask (Python web framework)

Blender & bpy (3D software & Python API)

SQLite (Inventory management database)

Git & GitHub (Version control)



