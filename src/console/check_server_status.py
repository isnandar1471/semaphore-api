import requests


import src.config.environment


try:
    requests.get(f"http://127.0.0.1:{src.config.environment.APP_SERVER_PORT}/")
    print("server on ready")
except Exception as e:
    error_string = f"servererror {e.args}"
    requests.get(f"{src.config.environment.APP_TELEGRAMBOT_URL}{error_string}")
    print(error_string)
