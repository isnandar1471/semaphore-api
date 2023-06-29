# from pydantic import BaseModel
# from fastapi import UploadFile


# class PredictionRequest(BaseModel):
#     file: UploadFile


# class PredictionResponse(BaseModel):
#     prediction: str


# class Response:
#     status: str
#     message: str

#     def __init__(self, status: str, message: str):
#         self.status = status
#         self.message = message

#     @staticmethod
#     def success(message: str) -> "Response":
#         return Response("success", message)

#     def error(message: str):
#         return Response("error", message)
