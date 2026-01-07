import os
import sys


from dotenv import load_dotenv


load_dotenv()


SECRET_KEY_STR = os.environ.get("FLASK_SECRET_KEY_STR")
if not SECRET_KEY_STR:
    print("❌ Secret Key is missing in .env file")
    sys.exit(1)
SECRET_KEY = SECRET_KEY_STR


FLASK_HOST_VALUE_STR = os.environ.get("FLASK_HOST_VALUE_STR")
if not FLASK_HOST_VALUE_STR:
    print("❌ FLASK_HOST_VALUE_STR is missing in .env file")
    sys.exit(1)
FLASK_HOST_VALUE = FLASK_HOST_VALUE_STR


FLASK_PORT_VALUE_STR = os.environ.get("FLASK_PORT_VALUE_INT")
if not FLASK_PORT_VALUE_STR:
    print("❌ FLASK_PORT_VALUE_INT is missing in .env file")
    sys.exit(1)
try:
    FLASK_PORT_VALUE_INT = int(FLASK_PORT_VALUE_STR)
except ValueError:
    print("❌ FLASK_PORT_VALUE_INT must be a valid integer")
    sys.exit(1)


value = os.environ.get("FLASK_DEBUG_BOOL", None)
if not value:
    print("❌ FLASK_DEBUG_BOOL must be 'True' or 'False' (string)")
    sys.exit(1)
if value == "True":
    FLASK_DEBUG_BOOL_bool = True
elif value == "False":
    FLASK_DEBUG_BOOL_bool = False
else:
    print("❌ FLASK_DEBUG_BOOL must be 'True' or 'False' (string)")
    sys.exit(1)


# Log file name
LOG_FILE_NAME_STR = os.environ.get("LOG_FILE_NAME_STR")
if not LOG_FILE_NAME_STR:
    print("❌ LOG_FILE_NAME_STR is missing in .env file")
    sys.exit(1)
LOG_FILE_NAME = LOG_FILE_NAME_STR


DATABASE_FILE_NAME_STR = os.environ.get("DATABASE_FILE_NAME_STR")
if not DATABASE_FILE_NAME_STR:
    print("❌ DATABASE_FILE_NAME is missing in .env file")
    sys.exit(1)
DATABASE_FILE_NAME = DATABASE_FILE_NAME_STR


if __name__ == "__main__":

    print(SECRET_KEY_STR)
    print(FLASK_HOST_VALUE_STR)
    print(FLASK_PORT_VALUE_INT)
    print(FLASK_DEBUG_BOOL_bool)
    print(type(FLASK_DEBUG_BOOL_bool))
    print(LOG_FILE_NAME_STR)
    print(DATABASE_FILE_NAME_STR)
