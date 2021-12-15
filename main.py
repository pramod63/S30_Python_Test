from fastapi import FastAPI, Depends, HTTPException, status
import models
import schemas
from sqlalchemy.orm import Session
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)  # Creates table in database


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")  # Get -- Operation
def root(db: Session = Depends(get_db)):  # Path operation function
    all_data = db.query(models.Record).all()
    return {"data": all_data}


@app.post("/create", status_code=201)
def create_address(request: schemas.Record, db: Session = Depends(get_db)):
    new_address = models.Record(name=request.name, long=request.long,
                                lat=request.lat)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return {"message": "Address created successfully..."}


@app.delete("/delete/{address_id}", status_code=204)
def delete_address(address_id, db: Session = Depends(get_db)):
    address = db.query(models.Record).filter(models.Record.id == address_id)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Address with ID={address_id} not found...")
    address.delete(synchronize_session=False)
    db.commit()
    return {"message": "Address deleted successfully..."}


@app.put("/update/{address_id}", status_code=202)
def root(address_id, request: schemas.Record, db: Session = Depends(get_db)):
    address = db.query(models.Record).filter(models.Record.id == address_id)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Address with ID={address_id} not found...")
    address.update({models.Record.name: request.name,
                    models.Record.lat: request.lat,
                    models.Record.long: request.long})
    db.commit()
    return {"message": "Address updated successfully..."}
