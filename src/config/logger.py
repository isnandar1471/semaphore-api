import logging
import datetime


formatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s")


file_handler = logging.FileHandler(f"logs/{datetime.date.today()}.log")
file_handler.setFormatter(formatter)


logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
