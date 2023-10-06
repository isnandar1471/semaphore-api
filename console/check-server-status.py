import requests
import os


import dotenv


dotenv_filepath = dotenv.find_dotenv(raise_error_if_not_found=True)

dotenv.load_dotenv(dotenv_path=dotenv_filepath)

try:
    requests.get(f"http://127.0.0.1:{os.getenv('APP_SERVER_PORT', '8888')}/")
    print("server on ready")
except Exception as e:
    error_string = f"servererror {e}"
    requests.get(f"{os.getenv('APP_TELEGRAMBOT_URL')}{error_string}")
    print(error_string)
