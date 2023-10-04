import os

CLASSES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DATABASE_URL_ENGINE = f"mysql+pymysql://{os.getenv('APP_DATABASE_USERNAME', 'root')}:{os.getenv('APP_DATABASE_PASSWORD', '')}@{os.getenv('APP_DATABASE_HOST', 'localhost')}:{os.getenv('APP_DATABASE_PORT', 3306)}/{os.getenv('APP_DATABASE_NAME', 'proyekakhir')}"
