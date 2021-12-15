from pydantic import BaseModel


class Record(BaseModel):
    name: str
    long: float
    lat: float
