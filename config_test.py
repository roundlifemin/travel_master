from dotenv import load_dotenv
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API _KEY is not set in the evnironment variables. Please set it in your .env file.")
else:
    print("OPENAI_API_KEY is set correctly.")

 
    