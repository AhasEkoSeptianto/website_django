import os
from dotenv import load_dotenv

load_dotenv()
SECRET_JWT=os.getenv('SECRET_JWT')