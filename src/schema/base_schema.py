import pydantic


class BaseSchema(pydantic.BaseModel):
    pass


class Ranking(BaseSchema):
    rank: int
    value: str
    probability: float
