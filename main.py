from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

@app.get("/cookies")
async def get_cookies():
    # Define the path to the cookies.json file
    file_path = "cookies.json"
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Cookies file not found")
    
    try:
        # Open and read the JSON file
        with open(file_path, "r") as json_file:
            cookies_data = json.load(json_file)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON format in cookies file")
    
    return cookies_data
