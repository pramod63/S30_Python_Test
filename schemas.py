from pydantic import BaseModel


class Record(BaseModel):
    name: str
    address: str
    long: float
    lat: float


class ShowData(BaseModel):
    name: str
    address: str

    class Config:
        orm_mode = True


class UserInput(BaseModel):
    distance: float
    long: float
    lat: float
