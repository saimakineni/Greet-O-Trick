from app import app
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv('.', '.env')
    app.run(port='5000', debug=True)