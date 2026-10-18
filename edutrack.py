from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()  # Load variables from .env file

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

response = supabase.table("students").select("*").execute()
print(response.data)
