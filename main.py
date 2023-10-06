import os


import uvicorn
import dotenv


dotenv.load_dotenv()


PORT = int(os.getenv("APP_SERVER_PORT", "8888"))


if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=PORT)
