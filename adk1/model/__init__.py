import os
from dotenv import load_dotenv # You might need to pip install python-dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(BASE_DIR, '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print(f"Warning: .env file not found at {dotenv_path}")

# Make the agent available when the package is imported
from . import agent

# You can also define a list of what to export when `from my_simple_agent import *` is used
__all__ = ['agent']