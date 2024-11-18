import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if the API key was loaded correctly
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please ensure your .env file is configured correctly.")
else:
    print("API key loaded successfully.")  # This will print the API key if it’s loaded
