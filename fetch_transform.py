import bpy
import requests

# Flask API URL
API_URL = "http://127.0.0.1:8000/transform"

def apply_transform():
    # Fetch transformation data from Flask API
    response = requests.post(API_URL, json={"object": "cube", "position": [1, 2, 3]})
    
    if response.status_code == 200:
        data = response.json()
        obj_name = data["data"]["object"]
        position = data["data"]["position"]

        # Check if object exists in Blender
        if obj_name in bpy.data.objects:
            obj = bpy.data.objects[obj_name]
            obj.location = position
            print(f"Updated {obj_name} position to {position}")

            # 🔹 Force Blender to refresh the viewport
            bpy.context.view_layer.update()  # Updates scene
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # Forces redraw

        else:
            print(f"Object '{obj_name}' not found in Blender!")

    else:
        print("Failed to fetch transformation data!")

# Run the function
apply_transform()
