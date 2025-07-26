# Decluttering an Email Project: Start-7/13/25

from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

print(f"EMAIL={EMAIL}, PASSWORD={'set' if PASSWORD else 'not set'}")

