import fastapi


from .router import route


app = fastapi.FastAPI()


app.include_router(router=route.router)
