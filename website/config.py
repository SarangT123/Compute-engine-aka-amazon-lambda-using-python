import os
from dotenv import load_dotenv

load_dotenv()

EDITOR = "nano"
TOKEN = os.environ.get("TOKEN")