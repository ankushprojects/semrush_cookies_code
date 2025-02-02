from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your Cloudflare Worker domain)
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],  # Allow all headers
)

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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    # Return the JSON data with the correct Content-Type header
    return cookies_data
