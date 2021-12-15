from database import Base
from sqlalchemy import Column, Integer, String, Numeric



class Record(Base):
    __tablename__ = "address_records"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    long = Column(Numeric(3, 15))
    lat = Column(Numeric(3, 15))

