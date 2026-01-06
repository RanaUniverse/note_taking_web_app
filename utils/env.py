import os
import sys


from dotenv import load_dotenv

load_dotenv()

SECRET_KEY_STR = os.environ.get("FLASK_SECRET_KEY_STR")
if not SECRET_KEY_STR:
    print("❌ Secret Key is missing in .env file")
    sys.exit(1)
print(SECRET_KEY_STR)
SECRET_KEY = SECRET_KEY_STR

# Log file name
LOG_FILE_NAME_STR = os.environ.get("LOG_FILE_NAME_STR")
if not LOG_FILE_NAME_STR:
    print("❌ LOG_FILE_NAME_STR is missing in .env file")
    sys.exit(1)
print(LOG_FILE_NAME_STR)
LOG_FILE_NAME = LOG_FILE_NAME_STR


DATABASE_FILE_NAME_STR = os.environ.get("DATABASE_FILE_NAME")
if not DATABASE_FILE_NAME_STR:
    print("❌ DATABASE_FILE_NAME is missing in .env file")
    sys.exit(1)
print(DATABASE_FILE_NAME_STR)

DATABASE_FILE_NAME = DATABASE_FILE_NAME_STR
