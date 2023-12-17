import uvicorn


import src.config.checker

src.config.checker.check_directories()
print("All directories have at least one file.")

src.config.checker.check_word_list()
print("Word list is valid.")


print("")
print("Load Environment Variables")
import src.config.environment


PORT = src.config.environment.APP_SERVER_PORT


if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=PORT, reload=True)
