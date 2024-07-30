import os
from dotenv import load_dotenv

load_dotenv()
back_env = os.getenv("BACK_ENV")
postgres_url = os.getenv("POSTGRES_URL")
os.environ["PYTHONPATH"] = os.getenv("PYTHONPATH", ".")
