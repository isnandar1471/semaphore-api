import requests
import os


import dotenv


dotenv_filepath = dotenv.find_dotenv()

if dotenv_filepath == "":
    print(".env file not found. using default value")

dotenv.load_dotenv(dotenv_path=dotenv_filepath)

is_success = False

try:
    requests.get(f'http://127.0.0.1:{os.getenv("APP_SERVER_PORT", "8888")}/')
except Exception as e:
    requests.get(f"https://api.telegram.org/bot6405514280:AAGs3xpeBAtoqAQqk-_-sUQqXGdhJ9nMOhY/sendMessage?chat_id=1150088790&text=servererror {e}")
    print("server error")
    print(e)
